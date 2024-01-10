from django.contrib import admin
from .models import *


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descriptions', 'group_muscle', 'photo')
    # list_display_links = ('id','name')
    # search_fields = ('name','group_muscle')


@admin.register(Vitamins)
class VitaminsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'disadvantage')
    list_display_links = ('id', 'name')
    #search_fields=('name')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'vitamins', 'descriptions', 'fats', 'proteins', 'carbohydrates', 'photo')
    #list_display_links=('id','name')
    #search_fields=('name')


# @admin.register(Users)
# class UsersAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     # list_display_links=('id','login')
#     # search_fields=('login','email')


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'date', 'day_of_week')
    # list_display_links=('id','date')
    # search_fields=('date','day_of_week')


@admin.register(BasketFood)
class BasketFoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_day', 'id_user', 'food_weight')
    list_display_links = ('id', 'id_day')


@admin.register(BasketExercise)
class BasketExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_exercise', 'id_day', 'id_user')
    #list_display_links=('id')

