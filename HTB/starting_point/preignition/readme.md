Hack the Box
Starting Point

Explosions

10.129.227.76

nmap -sV -sC --min-rate 1000 --max-retries 5 -oN nmap/explosions 10.129.227.76

Starting Nmap 7.80 ( https://nmap.org ) at 2023-06-18 00:30 Americas
Nmap scan report for 10.129.227.76
Host is up (0.12s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Welcome to nginx!

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.44 seconds

$ gobuster -u 10.129.227.76 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -x php,html,htm

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.129.227.76/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
[+] Status codes : 200,204,301,302,307,403
[+] Extensions   : php,html,htm
[+] Timeout      : 10s
=====================================================
2023/06/18 02:40:45 Starting gobuster
=====================================================
/admin.php (Status: 200)

http://10.129.227.76/admin.php

Try default username / password:
admin
admin

Success!

Admin Console Login
Congratulations! Your flag is: 6483bee07c1c1d57f14e5b0717503c73
