from django.urls import path
from . import views



urlpatterns=[
    path('home',views.customer_home),
    path('cart',views.customer_cart),
    path('productdetails',views.product_deatils),
    path('orders',views.my_order),
    path('passwordchange',views.change_password)
]