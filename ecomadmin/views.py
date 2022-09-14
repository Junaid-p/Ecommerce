from django.shortcuts import render

# Create your views here.
def approve_seller(request):
    return render(request,'admintemplates/approveseller.html')
def admin_home(request):
    return render(request,'admintemplates/home.html')
def admin_login(request):
    return render(request,'admintemplates/login.html')
def view_customer(request):
    return render(request,'admintemplates/viewcustomer.html')
def view_seller(request):
    return render(request,'admintemplates/viewseller.html')
def seller_order(request):
    return render(request,'admintemplates/viewsellerorder.html')