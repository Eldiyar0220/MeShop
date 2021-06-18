from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# def order(request):
#     return HttpResponse('hello This is order page')

from .forms import CreateOrderForms
from main.models import Products
from .models import Order


def create_order(request):
    product = Products.objects.all()
    print(request.POST)
    order_form = CreateOrderForms(request.POST)
    if order_form.is_valid():
        print(order_form.cleaned_data)
        # order = Order.objects.create(**order_form.cleaned_data)
        order_form.save()
        return redirect(product.get_absolute_url())


    order_form = CreateOrderForms()
    return render(request, 'order.html', {'form': order_form,
                                                'product': product})









