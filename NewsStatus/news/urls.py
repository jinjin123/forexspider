#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^index/$', views.index, name='news_index'),
]
