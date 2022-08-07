import os
os.system("curl http://45.136.197.234:5001/getipss -o ips.txt")
if os.path.exists("aips.txt") != True:
    os.system("iptables -I INPUT -p tcp --dport 6688 -j DROP")
    os.system("iptables -I INPUT -p udp --dport 6688 -j DROP")
    with open("ips.txt", "w") as fx:
        os.system("echo " ">>aips.txt")           
with open("ips.txt", "r", encoding="utf-8") as fp:
    ips = fp.read().split("\n")
with open("aips.txt", "r", encoding="utf-8") as fps:
    aips = fps.read().split("\n")
for ip in ips:
    if ip not in aips:
        os.system("iptables -I INPUT -s "+ip+" -p tcp --dport "+"6688"+" -j ACCEPT")
        os.system("iptables -I INPUT -s "+ip+" -p udp --dport "+"6688"+" -j ACCEPT")
        with open("aips.txt", "a", encoding="utf-8") as fp:
            fp.write(ip+"\n")
