from django.shortcuts import render



# Create your views here.
def seller_home(request):
    return render(request, 'sellertemplates/sellerhome.html')
def seller_cart(request):
    return render(request, 'sellertemplates/sellercart.html')
def seller_order(request):
    return render(request, 'sellertemplates/sellerorders.html')
def add_product(request):
    return render(request, 'sellertemplates/addproduct.html')
def change_password(request):
    return render(request, 'sellertemplates/changepassword.html')
def stoke_update(request):
    return render(request, 'sellertemplates/updatestoke.html')
