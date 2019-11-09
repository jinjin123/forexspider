# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import datetime
from news.models import News,Trump


def index(request):
    data = []
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    obj = News.objects.values("content","status").filter(time=today)
    #obj = Trump.objects.values("content","status").filter(exttime=today,status__isnull=True)
    data = [new for new in obj]
    rsp = {'data': data, 'msg': 'success'}
    return JsonResponse(rsp)
