from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def indexPageView(request) :
    return render(request, 'webpages/index.html')

def aboutPageView(request) :
    return render(request, 'webpages/about.html')
    
def tablePageView(request) :
    return render(request, 'webpages/table.html')

def resourcesPageView(request) :
    return render(request, 'webpages/resources.html')

def customerPageView(request) :
    return render(request, 'webpages/customer.html')