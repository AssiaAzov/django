from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request: HttpRequest):
    return render(request, "mainapp/index.html")

def contact(request: HttpRequest):
    return render(request, 'mainapp/contact.html')

def products(request: HttpRequest, id=0):
    return render(request, 'mainapp/products.html', {
        'product_id': id
    })

def layout(request: HttpRequest):
    return render(request, 'mainapp/layout.html')
