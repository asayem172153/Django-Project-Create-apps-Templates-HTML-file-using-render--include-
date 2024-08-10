from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def java(request):
    return HttpResponse('Java support OOP')

def python(request):
    return HttpResponse('Python support OOP')