apt update -y
apt install iptables,python3,screen -y
wget -P / https://raw.githubusercontent.com/HsGalaxy/MyResoursePool/main/autoIp.py /
echo "* * * * * python3 /autoIp.py" >> /var/spool/cron/crontabs/root
python3 /autoIp.py
python3 /autoIp.py
