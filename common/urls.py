from django.urls import path
from . import views


urlpatterns=[
    path('',views.common_index),
    path('changepassword',views.change_password),
    path('customerlogin',views.customer_login),
    path('customersignup',views.customer_signup),
    path('sellerlogin',views.seller_login),
    path('sellersignup',views.seller_signup),
    path('imgview',views.image_view)
]