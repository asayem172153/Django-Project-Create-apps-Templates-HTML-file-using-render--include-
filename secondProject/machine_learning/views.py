from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def supervised(request):
    return render(request,'machine_learning/supervised.html')

def unsupervised(request):
    return HttpResponse('Unsupervised Learning')
