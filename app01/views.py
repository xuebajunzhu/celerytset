from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from app01.tasks import add

def create_task(request):
    print('请求来了')
    result = add.delay(2,2)
    print('执行完毕')
    return HttpResponse(result.id)


def get_result(request):
    nid = request.GET.get('nid')
    from celery.result import AsyncResult
    # from demos.celery import app
    from celerytest import celery_app
    result_object = AsyncResult(id=nid, app=celery_app)
    # print(result_object.status)
    data = result_object.get()
    return HttpResponse(data)