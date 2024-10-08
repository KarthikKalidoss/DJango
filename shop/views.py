import json
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import *


# Create your views here.

# Home/Index
def home(request):
    products = Product.objects.filter(trending=1)
    return render(request, "shop/index.html", {'products': products})


# Login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully')
                return redirect("/")
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('/login')
        return render(request, "shop/login.html")


# Logout

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logout Successfully')
    return redirect('/')


# Register
def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registration Success. Please Login-in Now..')
            return redirect('/login')
    return render(request, "shop/register.html", {'form': form})


# Collections
def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, "shop/collections.html", {"category": category})


# Collection Views
def collections_view(request, name):
    if Category.objects.filter(name=name, status=0):
        products = Product.objects.filter(category__name=name)
        return render(request, "shop/products/index.html", {"products": products, "category_name": name})
    else:
        messages.warning(request, 'No Such Category Found')
        return redirect('collections')


# Product_details
def product_details(request, c_name, p_name):
    if Category.objects.filter(name=c_name, status=0):
        if Product.objects.filter(name=p_name, status=0):
            products = Product.objects.filter(name=p_name, status=0).first()
            return render(request, 'shop/products/product_details.html', {'products': products})
        else:
            messages.error(request, 'No Such Product Found')
            return redirect('collections')
    else:
        messages.error(request, 'No Such Category Found')
        return redirect('collections')


def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            print(data['product_qty'])
            print(data['pid'])
            print(request.user.id)
        else:
            return JsonResponse({'status': 'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status': 'invalid Access'}, status=200)
