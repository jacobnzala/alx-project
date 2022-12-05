from django.shortcuts import render
from .models import Category, Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'BuildAstore/home.html', {'products': products})