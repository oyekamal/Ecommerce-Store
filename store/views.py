from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.

def category(request):
    return {
        "categories": Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html',{'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/products/details.html", {"product":product})