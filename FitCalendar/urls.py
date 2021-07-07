from django.urls import path
from django.urls import path

from .views import *

urlpatterns=[
    path('',index, name='home'),
    path('product/',product.as_view(),name='product'),
    path('exercises/',exercises.as_view(),name='exercises'),
    path('exercises/new_exercises',new_exercises,name='new_exercises'),
    path('check_in/',RegisterUser.as_view(),name='check_in'),
    path('authorization/',authorization.as_view(),name='authorization'),

    path('logout/',logout_user,name='logout'),

    path('product/vitamins/',Vitamins.as_view(),name='Vitamins'),
    path('product/vitamins/new_vitamin',new_vitamin,name='new_vitamins'),
    path('profile/',profile,name='profile'),
    path('product/new_product',new_product,name='new_product'),

    # path('product/add_profile',add_profile,name='add_profile'),
    #path('delete/<int:id>/',delete_product,name='delete_product'),
]