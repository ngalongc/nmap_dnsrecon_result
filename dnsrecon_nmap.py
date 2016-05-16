import subprocess

host_ip_dict = {}
all_ip = []
# Determine ip is shared by which hostname
# Return a list of shared ip hostname
# print determine_hostname('1.2.3.4',_host_ip_dict)
#['www.esea.net', 'tv.esea.net', 'db.esea.net', 'play.esea.net', 'stem.esea.net', 'news.esea.net']

def determine_hostname(_ip,_host_ip_dict):
    shared_hostname = []
    for key in _host_ip_dict:
        for i in _host_ip_dict[key]:
            if i == _ip:
                shared_hostname.append(key)
    return shared_hostname

def fill_host_ip_dict():
    f = open('subdomains','r')
    arr = []
    for line in f.readlines():
        line = line.strip()
        arr = line.split(' ')
        ip = arr[4]
        hostname = arr[3]
        if host_ip_dict.has_key(hostname) == False:
            host_ip_dict[hostname] = [ip]
        else:
            old_ip_list = host_ip_dict[hostname]
            old_ip_list.append(ip)
            host_ip_dict[hostname] = old_ip_list
    f.close()
    for key in host_ip_dict:
        for i in host_ip_dict[key]:
            all_ip.append(i)

def main():
    fill_host_ip_dict()

    ip_set = set(all_ip)

    #Start nmap scan

    for i in list(ip_set):
        print "Start nmap scan with " + i
        hostname_shared = determine_hostname(i,host_ip_dict)
        pretty_hostname_shared = ""
        for j in hostname_shared:
            pretty_hostname_shared = j + "X" + pretty_hostname_shared
        output = subprocess.check_output('nmap --top-ports 1000 -oS %s %s' % (pretty_hostname_shared+i,i), shell=True)
        print output

main()
