


Executable is stripped. Need to find main function
$ gdb-gef
gef> r
- stop program (ctrl-c)
Now look at where the program stopped and look for 'main'
[#6] 0x7ffff7df018a → __libc_start_call_main(main=0x5555555551ec, argc=0x1, argv=0x7fffffffde48)

main=0x5555555551ec

Now set breakpoint at main:
gef> b *0x5555555551ec
gef> r

We need to find the address of this line of code:
    printf("Access Granted. \nEnter the navigation commands: ");
--> read(0,nav_commands,137);
    puts("Roger that!");

Show the next 70 lines of instructions:
gef> x/70i $pc

0x5555555552fc:	lea    rdi,[rip+0xe5e]        # 0x555555556161

Now set breakpoint where the application reads in 'nav_commands'
gef> break *0x5555555552fc


gef➤  r
Starting program: /home/kali/CTF/HTB/batcomputer/batcomputer 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Welcome to your BatComputer, Batman. What would you like to do?
1. Track Joker
2. Chase Joker
> 2
Ok. Let's do this. Enter the password: b4tp@$$w0rd!
Access Granted. 
Enter the navigation commands: DEADBEEF


gef➤  search-pattern DEADBEEF
[+] Searching 'DEADBEEF' in memory
[+] In '[stack]'(0x7ffffffde000-0x7ffffffff000), permission=rwx
  0x7fffffffdce4 - 0x7fffffffdcee  →   "DEADBEEF\n" 

So our input (DEADBEEF) is stored in memory starting at address
0x7fffffffdce4.
We need to figure out how many bytes between this address and the return address
in main.

** Now we need to look at the stack frames to see what addresses are where.
gef➤  i f
Stack level 0, frame at 0x7fffffffdd40:
 rip = 0x5555555552fc; saved rip = 0x7ffff7df018a
 called by frame at 0x7fffffffdde0
 Arglist at 0x7fffffffdcc8, args: 
 Locals at 0x7fffffffdcc8, Previous frame's sp is 0x7fffffffdd40
 Saved registers:
  rbp at 0x7fffffffdd30, rip at 0x7fffffffdd38

We can see the 'Saved registers: - rip at 0x7fffffffdd38'
So the return address is 0x7fffffffdd38.

Now subtract the start of our input (DEADBEEF) from the return address
to find how many bytes between them (so we can know how / where to overwrite)

gef➤  0x7fffffffdd38 - 0x7fffffffdce4
Undefined command: "0x7fffffffdd38".  Try "help".
gef➤  x 0x7fffffffdd38 - 0x7fffffffdce4
   0x54:	Cannot access memory at address 0x54

So there are 0x54 (84) bytes difference.