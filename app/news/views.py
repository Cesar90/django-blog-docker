from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(dir(request))
    return HttpResponse('Hello world')

def test(request):
    return HttpResponse('<h1>Test testing</h1>')