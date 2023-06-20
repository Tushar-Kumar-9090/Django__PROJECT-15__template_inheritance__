from django.shortcuts import render

# Create your views here.

def mdb_5(request):
    return render(request,'mdb_5.html')

def template_inheritance(request):
    return render(request,'template_inheritance.html')
