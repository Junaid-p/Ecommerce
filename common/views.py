from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'commontemplates/index.html')
def change_password(request):
    return render(request,'commontemplates/changepassword.html')
def customer_login(request):
    return render(request,'commontemplates/customerlogin.html')
def customer_signup(request):
    return render(request,'commontemplates/customersignup.html')
def seller_login(request):
    return render(request,'commontemplates/sellerlogin.html')
def seller_signup(request):
    return render(request,'commontemplates/sellersignup.html')
def image_view(request):
    return render(request,'commontemplates/image.html')
