
from django.urls import path

from .views import *

urlpatterns = [
   path('', index, name='home'),
   path('category/<str:slug>/', Category_detail_view.as_view(), name='category'),
   path('recipe-detail/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
   path('shop/', MainPageView.as_view(), name='shop'),
   path('about/', about, name='about'),
   path('contact/', contanct, name='contanct'),
   path('add-recipe/', add_recipe, name='add-recipe'),
   path('sumsungs/', sumsungs, name='sumsungs'),
   path('gome/', gome, name='gome'),
   path('corzina/', corzina, name='corzina'),
   path('More/', More, name='More'),
   # path('add-my-recipe/',  name='add-recipe')
]
