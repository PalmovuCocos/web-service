from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .models import *
def index(request):
    return render(request,'index.html',{'title':'Главная страница'})

def product(request):
    return render(request,'product.html',{'title':'Продукты'})

def exercises(request):
    exercise_list=exercise.object.all()
    return render(request,'exercises.html',{'exercise_list':exercise_list,'title':'Упражнения'})

def profile(request):
    return render(request,'profile.html',{'title':'Профиль'})

def check_in(request):
    return render(request,'check_in.html',{'title':'Вход и регистрация'})

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')