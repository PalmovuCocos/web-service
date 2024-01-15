from django.contrib import admin
from .models import *


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = '__all__'
    # list_display_links = ('id','name')
    # search_fields = ('name','group_muscle')


@admin.register(Vitamins)
class VitaminsAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links=('id','name')
    #search_fields=('name')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = '__all__'
    #list_display_links=('id','name')
    #search_fields=('name')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = '__all__'
    # list_display_links=('id','login')
    # search_fields=('login','email')


@admin.register(BasketFood)
class BasketFoodAdmin(admin.ModelAdmin):
    list_display= ('id', 'id_day', 'id_food_vit', 'id_food', 'id_vitamins', 'id_user', 'food_weight')
    list_display_links = ('id', 'id_day')


@admin.register(BasketExercise)
class BasketExerciseAdmin(admin.ModelAdmin):
    list_display = '__all__'
    #list_display_links=('id')

