from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html',{'products': products})