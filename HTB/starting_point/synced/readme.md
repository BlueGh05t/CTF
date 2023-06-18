Hack the Box
Starting Point

Synced

10.129.45.128

$ nmap -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/synced 10.129.45.128
Starting Nmap 7.80 ( https://nmap.org ) at 2023-06-18 04:19 Americas
Warning: 10.129.45.128 giving up on port because retransmission cap hit (2).
Nmap scan report for 10.129.45.128
Host is up (0.13s latency).
Not shown: 998 closed ports
PORT     STATE    SERVICE   VERSION
873/tcp  open     rsync     (protocol version 31)
1108/tcp filtered ratio-adp

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.41 seconds
