from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jspiders(request):
    return HttpResponse('<h1><center>JavaSpiders Branch, Bangalore, Karnataka</center></h1>')
