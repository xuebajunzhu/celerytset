# -*- coding:utf-8 -*-
# Author:cqk
# Data:2020/2/12 8:33
from celery import Celery

app = Celery('tasks', broker='redis://192.168.1.125:6381', backend='redis://192.168.1.125:6381')

@app.task
def x1(x, y):
    return x + y

@app.task
def x2(x, y):
    return x - y