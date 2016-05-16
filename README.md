# nmap_dnsrecon_result
A wrap up script to auto perform nmap scan from the result of dnsrecon, then output result with filename as hostname and ip

Example:
cat subdomain
[*] 	 A db.abc.net 104.16.94.3
[*] 	 A voip.abc.net 198.144.179.1
[*] 	 A puppet.abc.net 52.1.14.2

python dnsrecon_nmap.py
Start nmap scan with 198.144.179.022

Starting Nmap 7.01 ( https://nmap.org ) at 2016-05-16 23:07 CST
Nmap scan report for 198-144-179-109-host.colocrossing.com (198.144.179.119)
Host is up (0.23s latency).
Not shown: 994 closed ports
PORT      STATE    SERVICE
25/tcp    filtered smtp
139/tcp   filtered netbios-ssn
1068/tcp  filtered instl_bootc
6129/tcp  filtered unknown
50389/tcp open     unknown
65129/tcp open     unknown
.
.
.
.
.
ls -asl
4 -rw-r--r--  1 root root 1044 May 16 22:32 subdomains
4 -rw-r--r--  1 root root  454 May 16 23:07 voip.abc.netX198.144.179.109
4 -rw-r--r--  1 root root  333 May 16 23:11 zen.abc.netX52.1.122.83
