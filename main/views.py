from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def category_detail(request, slug):
    return render(request, 'category-detail.html')
