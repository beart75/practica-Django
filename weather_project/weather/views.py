from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>hello world again</h1>")