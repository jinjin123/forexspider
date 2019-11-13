FROM centos:7
RUN yum install python3 -y 
RUN yum install -y gcc  \
	gcc-c++ \
    	openssh-server \
	openssh-*


ADD trump.py /root/trump.py

ADD run.sh /run.sh
RUN chmod 777 /run.sh 

ADD requirements.txt /etc/
RUN pip3 install -r  /etc/requirements.txt

RUN cp  /usr/local/lib64/python3.6/site-packages/configparser.py  /usr/local/lib64/python3.6/site-packages/ConfigParser.py

RUN pip3 install MySQL-python

RUN echo "*/15 * * *  /usr/bin/python  /root/project/trump.py  > /dev/null 2>&1 " > /var/spool/cron/crontabs/root

EXPOSE 22
WORKDIR /
CMD ["./run.sh"]
