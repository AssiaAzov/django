from django.shortcuts import render
from django.http import HttpRequest
from .models import ProductCategory, Product


# Create your views here.
def index(request: HttpRequest):
    products = Product.objects.all()[:4]
    content = {'products': products}
    return render(request, 'mainapp/index.html', content)

def contact(request: HttpRequest):
    return render(request, 'mainapp/contact.html')

def products(request: HttpRequest):
    products = Product.objects.all()[:4]
    content = {'products': products}
    return render(request, 'mainapp/products.html', content)

def layout(request: HttpRequest):
    return render(request, 'mainapp/layout.html')
