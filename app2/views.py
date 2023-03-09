from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pyspiders(request):
    return HttpResponse('<h1><marquee>PythonSpiders Branch, Bangalore, Karnataka</marquee></h1>')