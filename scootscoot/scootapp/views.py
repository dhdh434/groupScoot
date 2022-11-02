from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def indexPageView(request) :
    return HttpResponse('Scoot Scoot!!!')

def aboutPageView(request) :
    return HttpResponse('About!!')
    
def tablePageView(request) :
    return HttpResponse('Tables Yum!!!')

def resourcesPageView(request) :
    return HttpResponse('Resources!!!')

def customerPageView(request) :
    return HttpResponse('customer!!!')