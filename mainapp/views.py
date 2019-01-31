from django.shortcuts import render
from django.http import HttpRequest
from .models import ProductCategory, Product
import datetime


# Create your views here.
def index(request: HttpRequest):
    products = Product.objects.all()[:4]
    content = {'title': title,'products': products}
    return render(request, 'mainapp/index.html', content)

def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@geekshop.ru',
            'address': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivostok@geekshop.ru',
            'address': 'Близко к океану',
        },
    ]
    content = {'title': title, 'visit_date':visit_date, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()[3:5]

    content = {'title': title, 'links_menu': links_menu, 'same_products': same_products}
    return render(request, 'mainapp/products.html', content)

def layout(request: HttpRequest):
    return render(request, 'mainapp/layout.html')

from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm

def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

def edit(request):

    return HttpResponseRedirect(reverse('main'))

def register(request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)

def edit(request):
    title = 'редактирование'
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
           edit_form.save()
           return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)
