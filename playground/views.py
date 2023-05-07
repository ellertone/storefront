from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
#takes a requests and  returns a response

def say_hello(request):
    return HttpResponse('Hello World')