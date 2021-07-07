from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

# class AddUserForm(forms.Form):
#     type_body_choices=(
#     ('1','Эктоморф'),
#     ('2','Мезоморф'),
#     ('3','Эндоморф'),
# )
#     sex_type=(
#         ('1','М'),
#         ('2','Ж')
#     )
#     login=forms.CharField(max_length=80, label='Логин')
#     email=forms.EmailField(max_length=80, label='Email')
#     password=forms.CharField(max_length=30, label='Пароль')
#     sex=forms.ChoiceField(choices=sex_type, widget=forms.RadioSelect(), label='Пол')
#     weight=forms.IntegerField(label='Вес',required=False)
#     height=forms.IntegerField(label='Рост',required=False)
#     type_body=forms.ChoiceField(choices =type_body_choices)
#     target=forms.CharField(max_length=30, label='Цель',required=False)
    

class CheckUserForm(forms.Form):
    login=forms.CharField(max_length=80, label='Логин')
    password=forms.CharField(max_length=30, label='Пароль')

class AddProduct(forms.ModelForm):
    class Meta:
        model=food
        fields=['name','descriptions','fats','proteins','carbohydrates','photo']
        widgets={
            'descriptions': forms.Textarea(attrs={'cols':60,'rows':10})
        }

class AddVitamin(forms.ModelForm):
    class Meta:
        model=vitamins
        fields=['name','role','disadvantage']

class AddExercises(forms.ModelForm):
    class Meta:
        model=exercise
        fields=['name','descriptions','group_muscle','photo']
        widgets={
            'descriptions': forms.Textarea(attrs={'cols':60,'rows':10})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин: ', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email: ', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль: ', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля: ', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class authorizationForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
 
# class add_profile(forms.ModelForm):
#     class Meta:
#         model=users
#         fields=['weight','height','type_body','target','fats','proteins','carbohydrates','sex']

# class AddBasketProduct(forms.ModelForm):
#     date=forms.DateField(label='Выберете день')