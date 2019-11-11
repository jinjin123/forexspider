# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    title = models.CharField( max_length=100, null=True,verbose_name='标题')
    link = models.CharField( max_length=100, null=True,verbose_name='link')
    content = models.CharField( max_length=100,null=True, verbose_name='内容')
    time = models.DateField(db_index=True,null=True, verbose_name='日期')
    status = models.IntegerField(null=True, verbose_name='状态')
    
    class Meta:
        db_table = 'news'

    @property
    def to_dict(self):
        return {
            'content': self.content,
            'status': self.status
        }

class Trump(models.Model):
    content = models.CharField( max_length=100,null=True, verbose_name='内容')
    tag = models.CharField( max_length=100,null=True, verbose_name='标记')
    time = models.DateTimeField(db_index=True,null=True, verbose_name='日期')
    exttime = models.DateField(db_index=True,null=True, verbose_name='日期')
    status = models.IntegerField(null=True, verbose_name='状态')
    
    class Meta:
        db_table = 'trump'

    @property
    def to_dict(self):
        return {
            'content': self.content,
            'status': self.status
            }

class Jten(models.Model):
    content = models.CharField( max_length=100,null=True, verbose_name='内容')
    tag = models.CharField( max_length=100,null=True, verbose_name='标记')
    time = models.DateTimeField(db_index=True,null=True, verbose_name='日期')
    exttime = models.DateField(db_index=True,null=True, verbose_name='日期')
    status = models.IntegerField(null=True, verbose_name='状态')
    
    class Meta:
        db_table = 'jten'

    @property
    def to_dict(self):
        return {
            'content': self.content,
            'status': self.status
            }
