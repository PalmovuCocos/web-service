from django.urls import path, register_converter
from django.urls import path
from .convertors import FourDigitYearConverter

from .views import *

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', index, name='home'),
    path('product/', product.as_view(), name='product'),
    path('exercises/', exercises.as_view(), name='exercises'),
    path('exercises/new_exercises', new_exercises, name='new_exercises'),
    path('check_in/', RegisterUser.as_view(), name='check_in'),
    path('authorization/', authorization.as_view(), name='authorization'),
    path('logout/', logout_user, name='logout'),
    path('product/vitamins/', Vitamins.as_view(), name='Vitamins'),
    path('product/vitamins/new_vitamin', new_vitamin, name='new_vitamins'),
    path('profile/', profile, name='profile'),
    path('product/new_product', new_product, name='new_product'),

    path('test/<year4:cat_id>/', test_view, name='test'),

]