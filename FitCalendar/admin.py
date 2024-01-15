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
    list_display_links = ('id', 'name', 'role')
    #search_fields=('name')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'vitamins', 'descriptions', 'fats', 'proteins',
                    'carbohydrates', 'photo')
    #list_display_links=('id','name')
    #search_fields=('name')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height')
    # list_display_links=('id','login')
    # search_fields=('login','email')


@admin.register(BasketFood)
class BasketFoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'user', 'day', 'food_weight')
    list_display_links = ('id', )


@admin.register(BasketExercise)
class BasketExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise', 'day', 'user')
    #list_display_links=('id')


@admin.register(VitaminsInFood)
class VitaminsInFoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'vitamins', 'food', 'quantity')
