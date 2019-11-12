FROM paddlepaddle/paddle:latest-gpu-cuda10.0-cudnn7

RUN apt-get install vim -y
RUN  apt-get install supervisor -y
RUN  apt-get install libmysqlclient-dev -y

RUN pip install paddlehub

ADD __init__.py /usr/local/lib/python2.7/dist-packages/paddlehub/dataset/

ADD demodataset.py /usr/local/lib/python2.7/dist-packages/paddlehub/dataset/

RUN mkdir -p /root/dataset/
ADD dev.tsv  /root/dataset/
ADD test.tsv  /root/dataset/
ADD train.tsv  /root/dataset/

ADD requirements.txt /etc/
RUN pip install -r  /etc/requirements.txt

RUN mkdir -p /root/project/

ADD supervisord.conf /etc/
ADD gunicorn.conf /etc/

#RUN mkdir -p /var/{log/supervior,log/gunicorn,run/supervisord}

ADD startup.sh /startup.sh
RUN chmod +x /startup.sh

EXPOSE 8000 9001



ENTRYPOINT ["/startup.sh"]
WORKDIR  /root/project/news


