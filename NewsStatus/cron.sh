#!/bin/bash
if [ $1 = 'stop' ];then
	beatp=`ps gaux | grep 'celery beat' | grep -v grep | awk '{print $2}'`
	workp=`ps gaux | grep 'celery worker' | grep -v grep | awk '{print $2}'`
	kill -9 $beatp 
	kill -9 $workp
	exit 0
fi

if [ $1 = 'restart' ];then
	beatp=`ps gaux | grep 'celery beat' | grep -v grep | awk '{print $2}'`
	workp=`ps gaux | grep 'celery worker' | grep -v grep | awk '{print $2}'`
	kill -9 $beatp
	kill -9 $workp
	nohup python manage.py celery worker -l info >>logs/cronwork.log 2>&1 &
	nohup python manage.py celery beat >>logs/cronbeat.log 2>&1 &
	exit 0
fi

if [ $1 = 'start' ];then
	nohup python manage.py celery worker   -l info >>logs/cronwork.log 2>&1 &
	nohup python manage.py celery beat --pidfile=logs/bpid >>logs/cronbeat.log 2>&1 &
	exit 0
fi

echo "args:stop|start|restart"

exit 0
