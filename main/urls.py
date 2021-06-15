
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name='category'),
    path('about/', about, name='about'),
    path('contact/', contanct, name='contanct')
]
