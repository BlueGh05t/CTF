optimistic

$ file optimistic
optimistic: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=24f4b065a2eab20657772e85de2af83b2f6fe8b1, for GNU/Linux 3.2.0, not stripped

$ checksec --file optimistic
[*] '/home/kali/CTF/HTB/optimistic/optimistic'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments



printf("Great! Here\'s a small welcome gift: %p\n",&stack0xfffffffffffffff8);


The string "Great! Here\'s a small welcome gift: %p\n" will be loaded into RDI
The next argument will be held in RSI (i.e. &stack0xfffffffffffffff8)

Here we see that RBP (stack base pointer) is copied into RAX
Then, RAX is copied into RSI.

So, stack0xfffffffffffffff8 points to the stack base pointer.

00101293 48 89 e8        MOV        RAX,RBP
00101296 48 89 c6        MOV        RSI,RAX
00101299 48 8d 3d        LEA        RDI,[s_Great!_Here's_a_small_welcome_gi_001020   = "Great! Here's a small welcome
00 0e 00 00
001012a0 b8 00 00        MOV        enroll_int,0x0
00 00




  len_read = read(0,user_email_buff,8);
  email_len = (undefined2)len_read;
  printf("Age: ");
  len_read = read(0,user_age_buff,8);
  age_len = (undefined4)len_read;
  printf("Length of name: ");
  __isoc99_scanf(&DAT_00102104,&name_len);
  if (64 < (int)name_len) {
    puts("Woah there! You shouldn\'t be too optimistic.");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  printf("Name: ");
  len_read = read(0,user_name_buff,(ulong)name_len);
  name_len = 0;


name_len needs to be < 64

Then len(name) - 9 needs to be greater than name_len entered