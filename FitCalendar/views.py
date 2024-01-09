from django.contrib.auth import logout
from django.views.generic.dates import DateMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from FitCalendar.forms import *
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound#,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .utils import *
def index(request):
    return render(request,'index.html',{'title':'Главная страница'})



class product(ListView):#вывод страницы о еде 
    model=food  
    template_name='product.html'
    extra_context={'title':'Продукты'}

def new_product(request):# вывод страницы с формой на добавление продкута 
    if (request.method=='POST'):
        form_new_product=AddProduct(request.POST, request.FILES)
        if form_new_product.is_valid():
            try:
                #print(form_new_product.cleaned_data)
                form_new_product.save()
                return redirect('product')
            except:form_new_product.add_error(None,'Ошибка добавления продукта')
            
    else:
        form_new_product=AddProduct()    
    return render(request,'new_product.html',{'form_new_product':form_new_product,'title':'Добавление нового продукта'})

# def delete_product(request, id):
#     try:
#         Product = food.objects.get(pk=id)
#         Product.delete()
#         return redirect("product")
#     except food.DoesNotExist:
#         return HttpResponseNotFound("<h2>Продукт не наайден</h2>")



# class new_product(CreateView):
#     form_class=AddProduct
#     template_name='new_product.html'
#     extra_context={'title':'Добавление нового продукта'}
#     context_object_name='form_new_product'

class Vitamins(ListView):#вывод страницы с витаминами 
    model=vitamins
    template_name='Vitamins.html'
    extra_context={'title':'Витамины'}

def new_vitamin(request):# вывод страницы с формой на добавление витамина 
    if (request.method=='POST'):
        form_new_vitamin=AddVitamin(request.POST, request.FILES)
        if form_new_vitamin.is_valid():
            try:
                #print(form_new_product.cleaned_data)
                form_new_vitamin.save()
                return redirect('Vitamins')
            except:form_new_vitamin.add_error(None,'Ошибка добавления витамина')
            
    else:
        form_new_vitamin=AddVitamin()    
    return render(request,'new_vitamins.html',{'form_new_vitamin':form_new_vitamin,'title':'Добавление нового витамина'})

def exercises(request):# вывод страницы с упражнениями 
    exercise_list=exercise.objects.all()
    return render(request,'exercises.html',{'exercise_list':exercise_list,'title':'Упражнения'})

class exercises(ListView):#вывод страницы с витаминами 
    model=exercise
    template_name='exercises.html'
    extra_context={'title':'Упражнения'}

def new_exercises(request):# вывод страницы с формой на добавление упражнения 
    if (request.method=='POST'):
        form_new_exercises=AddExercises(request.POST, request.FILES)
        if form_new_exercises.is_valid():
            try:
                form_new_exercises.save()
                return redirect('exercises')
            except:form_new_exercises.add_error(None,'Ошибка добавления упражнения')
            
    else:
        form_new_exercises=AddExercises()    
    return render(request,'new_exercises.html',{'form_new_exercises':form_new_exercises,'title':'Добавление нового упражнения'})


def profile(request): #вывод информации о пользователе
    return render(request, 'profile.html', {'title':'Профиль'})


class RegisterUser(DateMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'check_in.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class authorization(DateMixin, LoginView):
    form_class = authorizationForm
    template_name = 'authorization.html'
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('add_profile')

# def add_profile(request): # вывод страницы с формой на добавление профиля 
#     if (request.method=='POST'):
#         form_new_profile=add_profile(request.POST, request.FILES)
#         if form_new_profile.is_valid():
#             try:
#                 form_new_profile.save()
#                 return redirect('home')
#             except:form_new_profile.add_error(None,'Ошибка добавления профиля')
            
#     else:
#         form_new_exercises=AddExercises()    
#     return render(request,'add_profile.html',{'form_new_profile':form_new_profile,'title':'Добавление нового профиля'})
 
def logout_user(request):
    logout(request)
    return redirect('authorization')

def pageNotFound(request,exception): 
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')