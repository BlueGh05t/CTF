ROPEmporium
write4 - 64bit

Initially unable to determine way forward.  Watched CryptoCat's video for help

Need to find a place in memory (writable memory) to write our string (flag.txt)
To do this, we need some gadgets to help out.

ropper -- --search "mov"

pwndbg> disass usefulFunction
Dump of assembler code for function usefulFunction:
   0x0000000000400617 <+0>:	push   rbp
   0x0000000000400618 <+1>:	mov    rbp,rsp
   0x000000000040061b <+4>:	mov    edi,0x4006b4
   0x0000000000400620 <+9>:	call   0x400510 <print_file@plt>
   0x0000000000400625 <+14>:	nop
   0x0000000000400626 <+15>:	pop    rbp
   0x0000000000400627 <+16>:	ret

   	pwndbg> disassemble usefulGadgets
Dump of assembler code for function usefulGadgets:
   0x0000000000400628 <+0>:	mov    QWORD PTR [r14],r15
   0x000000000040062b <+3>:	ret
   0x000000000040062c <+4>:	nop    DWORD PTR [rax+0x0]
End of assembler dump.

This function (usefulGadgets) has a useful gadget we can use:
0x0000000000400628 <+0>:	mov    QWORD PTR [r14],r15

So we'll need to find 'pop r15' somewhere in the program

pwndbg> info target
Symbols from "/home/blue/Projects/BlueGh05t/CTF/ropemporium/write4/write4".
Local exec file:
	`/home/blue/Projects/BlueGh05t/CTF/ropemporium/write4/write4', file type elf64-x86-64.
	Entry point: 0x400520
	0x0000000000400238 - 0x0000000000400254 is .interp
	0x0000000000400254 - 0x0000000000400274 is .note.ABI-tag
	0x0000000000400274 - 0x0000000000400298 is .note.gnu.build-id
	0x0000000000400298 - 0x00000000004002d0 is .gnu.hash
	0x00000000004002d0 - 0x00000000004003c0 is .dynsym
	0x00000000004003c0 - 0x000000000040043c is .dynstr
	0x000000000040043c - 0x0000000000400450 is .gnu.version
	0x0000000000400450 - 0x0000000000400470 is .gnu.version_r
	0x0000000000400470 - 0x00000000004004a0 is .rela.dyn
	0x00000000004004a0 - 0x00000000004004d0 is .rela.plt
	0x00000000004004d0 - 0x00000000004004e7 is .init
	0x00000000004004f0 - 0x0000000000400520 is .plt
	0x0000000000400520 - 0x00000000004006a2 is .text
	0x00000000004006a4 - 0x00000000004006ad is .fini
	0x00000000004006b0 - 0x00000000004006c0 is .rodata
	0x00000000004006c0 - 0x0000000000400704 is .eh_frame_hdr
	0x0000000000400708 - 0x0000000000400828 is .eh_frame
	0x0000000000600df0 - 0x0000000000600df8 is .init_array
	0x0000000000600df8 - 0x0000000000600e00 is .fini_array
	0x0000000000600e00 - 0x0000000000600ff0 is .dynamic
	0x0000000000600ff0 - 0x0000000000601000 is .got
	0x0000000000601000 - 0x0000000000601028 is .got.plt
	0x0000000000601028 - 0x0000000000601038 is .data
	0x0000000000601038 - 0x0000000000601040 is .bss

	Data section starts at 0x601028

	pwndbg> ropper -- --search pop
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop

[INFO] File: /home/blue/Projects/BlueGh05t/CTF/ropemporium/write4/write4
0x000000000040068c: pop r12; pop r13; pop r14; pop r15; ret; 
0x000000000040068e: pop r13; pop r14; pop r15; ret; 
0x0000000000400690: pop r14; pop r15; ret; 
0x0000000000400692: pop r15; ret; 
0x000000000040057b: pop rbp; mov edi, 0x601038; jmp rax; 
0x000000000040068b: pop rbp; pop r12; pop r13; pop r14; pop r15; ret; 
0x000000000040068f: pop rbp; pop r14; pop r15; ret; 
0x0000000000400588: pop rbp; ret; 
0x0000000000400693: pop rdi; ret; 
0x0000000000400691: pop rsi; pop r15; ret; 
0x000000000040068d: pop rsp; pop r13; pop r14; pop r15; ret; 


ROPE{a_placeholder_32byte_flag!}
