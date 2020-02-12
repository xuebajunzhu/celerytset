from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import HttpResponse
from app01.tasks import add,mul
from celery.result import AsyncResult
# from demos.celery import app
from celerytest import celery_app

def create_add_task(request):
    print('请求来了')
    result = add.delay(2,2)
    print('执行完毕')
    print(result.id)
    result_object = AsyncResult(id=result.id, app=celery_app)

    data = result_object.get()
    print(data)
    return HttpResponse(data)



def create_mul_task(request):
    ctime = datetime.datetime.now()
    utc_ctime = datetime.datetime.utcfromtimestamp(ctime.timestamp())

    s10 = datetime.timedelta(seconds=20)
    ctime_x = utc_ctime + s10

    # 使用apply_async并设定时间
    result = mul.apply_async(args=[2, 3], eta=ctime_x)
    print(result.id)
    return HttpResponse(result.id)




"""
from datetime import datetime

v1 = datetime(2017, 4, 11, 3, 0, 0)
print(v1)

v2 = datetime.utcfromtimestamp(v1.timestamp())
print(v2)

"""
