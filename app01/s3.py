# -*- coding:utf-8 -*-
# Author:cqk
# Data:2020/2/12 8:33

from celery.result import AsyncResult
from .s1 import app

result_object = AsyncResult(id="任务ID", app=app)
print(result_object.status)