from django.contrib import admin
from .models import *
class ExerciseAdmin(admin.ModelAdmin):
    list_display=('id','name','descriptions','group_muscle','photo')
    list_display_links=('id','name')
    search_fields=('name','group_muscle')
class vitaminsAdmin(admin.ModelAdmin):
    list_display=('id','name','role','disadvantage')
    list_display_links=('id','name')
    #search_fields=('name')
class foodAdmin(admin.ModelAdmin):
    list_display=('id','name','descriptions','fats','proteins','carbohydrates','photo')
    #list_display_links=('id','name')
    #search_fields=('name')
class usersAdmin(admin.ModelAdmin):
    list_display=('id','weight','height','type_body','target','fats','proteins','carbohydrates','sex')
    # list_display_links=('id','login')
    # search_fields=('login','email')
class dayAdmin(admin.ModelAdmin):
    list_display=('id','date','day_of_week')
    list_display_links=('id','date')
    search_fields=('date','day_of_week')
class food_vitAdmin(admin.ModelAdmin):
    list_display=('id','id_food','id_vitamins')
    #list_display_links=('id')
    #search_fields=('id_food','id_vitamins')
class basket_foodAdmin(admin.ModelAdmin):
    list_display=('id','id_day','id_food_vit','id_food','id_vitamins','id_user','food_weight')
    list_display_links=('id','id_day')
class basket_exerciseAdmin(admin.ModelAdmin):
    list_display=('id','id_exercise','id_day','id_user')
    #list_display_links=('id')
admin.site.register(exercise,ExerciseAdmin)
admin.site.register(vitamins,vitaminsAdmin)
admin.site.register(food,foodAdmin)
admin.site.register(users,usersAdmin)
admin.site.register(day,dayAdmin)
admin.site.register(food_vit,food_vitAdmin)
admin.site.register(basket_food,basket_foodAdmin)
admin.site.register(basket_exercise,basket_exerciseAdmin)
# Register your models here.
