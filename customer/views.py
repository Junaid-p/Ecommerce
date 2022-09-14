import re
from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer_template/home.html')
def customer_cart(request):
    return render(request,'customer_template/cart.html')
def product_deatils(request):
    return render(request, 'customer_template/productdetail.html')
def my_order(request):
    return render(request,'customer_template/myorders.html')
def change_password(request):
    return render(request, 'customer_template/changepassword.html')