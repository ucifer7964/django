from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def nigamView(request):
    data="<h1>This is Akash nigam first project</h1>"
    return HttpResponse(data)

def nigam2view(request):
    data="<h1>this is second view</h1>"
    return HttpResponse(data)    