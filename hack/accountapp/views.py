from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    #return HttpResponse('Hello world!')
    return render(request, 'accountapp/helloworld.html')

