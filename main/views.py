from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def category_detail(request, slug):
    return render(request, 'category-detail.html')

def about(request):
    return render(request, 'about.html')


def contanct(request):
    return render(request, 'contact.html')


