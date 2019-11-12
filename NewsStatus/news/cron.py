# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


from NewsStatus.celery import app
from news.models import News,Trump,Jten
from news.base import AibaseApi
import datetime
import numpy as np
import os
import time


def static_news():
        ai = AibaseApi()
        cls_task = ai.load()
        data = []
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        obj = News.objects.values("content","status").filter(time=today,status__isnull=True)
        data = [list(new.values()) for new in obj]
        ndex = 0
        run_states = cls_task.predict(data=data)
        results = [run_state.run_results for run_state in run_states]
        for batch_result in results:
            batch_result = np.argmax(batch_result, axis=2)[0]
            for result in batch_result:
                News.objects.filter(content=data[index][0]).update(status=int(result))
                index += 1

def trump_news():
        ai = AibaseApi()
        cls_task = ai.load()
        data = []
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        obj = Trump.objects.values("content","status").filter(exttime=today,status__isnull=True)
        data = [list(new.values()) for new in obj]
        index = 0
        run_states = cls_task.predict(data=data)
        results = [run_state.run_results for run_state in run_states]
        for batch_result in results:
            batch_result = np.argmax(batch_result, axis=2)[0]
            for result in batch_result:
                Trump.objects.filter(content=data[index][0]).update(status=int(result))
                index += 1

def jten_news():
        ai = AibaseApi()
        cls_task = ai.load()
        data = []
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        obj = Jten.objects.values("content","status").filter(exttime=today,status__isnull=True)
        data = [list(new.values()) for new in obj]
        index = 0
        run_states = cls_task.predict(data=data)
        results = [run_state.run_results for run_state in run_states]
        for batch_result in results:
            batch_result = np.argmax(batch_result, axis=2)[0]
            for result in batch_result:
                Jten.objects.filter(content=data[index][0]).update(status=int(result))
                index += 1
