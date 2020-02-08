#!/bin/bash
/bin/echo  "* * * * * sleep 15;/usr/bin/python /root/project/news/news/jten.py > /dev/null 2>&1" > /var/spool/cron/crontabs/root
/bin/echo  "*/15 * * * * /usr/bin/python /root/project/news/news/trumpnew.py  > /dev/null 2>&1" >> /var/spool/cron/crontabs/root
/bin/echo  "* 22 * * * /usr/bin/python /root/project/news/news/staticnew.py  > /dev/null 2>&1" >> /var/spool/cron/crontabs/root
service cron restart
