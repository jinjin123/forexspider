# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .forms import jForm
import datetime
import json
from news.models import News,Trump,Jten


def index(request):
    data = []
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    obj = News.objects.values("content","status").filter(time=today)
    data = [new for new in obj]
    rsp = {'data': data, 'msg': 'success',"count": len(data)}
    return JsonResponse(rsp)

def trump_news(request):
    data = []
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    obj = Trump.objects.values("content","status","time").filter(exttime=today,status__isnull=False).order_by('-time')
    data = [new for new in obj]
    rsp = {'data': data, 'msg': 'success'}
    return JsonResponse(rsp)


def jten(request):
    rsp = {'data':"", 'msg': 'success'}
    if request.method == "POST":
        data = json.loads(request.body)
        row = Jten.objects.filter(tag=data["tag"])
        if  row.count()  == 0:
            Jten.objects.create(content=data["content"],tag=data["tag"],exttime=data["exttime"],time=data["time"])
        return JsonResponse(rsp)
    

def jten_off(request):
    if request.method == "POST":
        data = json.loads(request.body)
	limit = int(data["limit"])
	offset = int(data["limit"])
    	today = datetime.datetime.now().strftime('%Y-%m-%d')
    	obj = Jten.objects.values("content","status","time").filter(exttime=today,status__isnull=False).order_by('-time')[offset:(offset + limit)]
    	data = [new for new in obj]
    	rsp = {
		"data": data,
		 'msg': 'success',
		"total": Jten.objects.filter(exttime=today,status__isnull=False).count()
	 }
    	return JsonResponse(rsp)

