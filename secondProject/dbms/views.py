from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def database(request):
    return render(request,'dbms/database.html')

def sql(request):
    return HttpResponse('SQL is essential for Database')
