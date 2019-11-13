#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^index/$', views.index, name='news_index'),
    url(r'^trump/$', views.trump_news, name='trump_news'),
    url(r'^jten/$', views.jten, name='jten'),
    url(r'^jten_off/$', views.jten_off, name='jten_off'),
]
