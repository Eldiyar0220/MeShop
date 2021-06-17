from django.shortcuts import render

from .models import Category, Products


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}



def get_productes(request):
    products = Products.objects.all()
    return {'products': products}