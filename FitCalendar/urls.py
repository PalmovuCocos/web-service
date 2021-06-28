from django.urls import path
from django.urls import path

from .views import *

urlpatterns=[
    path('',index, name='home'),
    path('product/',product,name='product'),
    path('exercises/',exercises,name='exercises'),
    path('check_in/',check_in,name='check_in'),

]