# -*- coding:utf-8 -*-
# Author:cqk
# Data:2020/2/12 7:34
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y