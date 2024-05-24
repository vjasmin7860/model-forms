from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('data is done')
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EFWO=WebpageForm()
    d={'EFWO':EFWO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('webpage is created successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_webpage.html',d)


def insert_AccessRecord(request):
    EFAO=AccessRecordForm()
    d={'EFAO':EFAO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('accessrecord is created successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_AccessRecord.html',d)