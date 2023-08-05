Hack the Box
starting point

Ignition


curl -v http://10.129.1.27
*   Trying 10.129.1.27:80...
* Connected to 10.129.1.27 (10.129.1.27) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.129.1.27
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Server: nginx/1.14.2
< Date: Mon, 26 Jun 2023 01:03:46 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Set-Cookie: PHPSESSID=sva9oc3atohb41fvc4gfr0pm4s; expires=Mon, 26-Jun-2023 02:03:46 GMT; Max-Age=3600; path=/; domain=10.129.1.27; HttpOnly; SameSite=Lax
< Location: http://ignition.htb/

gobuster -u http://ignition.htb -w /usr/share/wordlists/Discovery/Web-Content/directory-list-2.3-small.txt


The default username for your Magento router is admin. 
The default password is 123123. 
Enter the username & password, hit "Enter" 

head /usr/share/wordlists/Passwords/probable-v2-top1575.txt 
123456
password
123456789
12345678
12345
qwerty
123123
111111
abc123
1234567

*** Try each of these with 123 appended (since the default is 123123)

Username: admin
Password: qwerty123


Advanced Reporting
Congratulations, your flag is: 797d6c988d9dc5865e010b9410f247e0
Gain new insights and take command of your business' performance, using our dynamic product, order, and customer reports tailored to your customer data.

