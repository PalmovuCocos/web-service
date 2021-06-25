from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    return HttpResponse("Hello World")
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')