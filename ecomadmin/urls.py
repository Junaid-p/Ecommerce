from django.urls import path
from . import views


urlpatterns=[
    path('approve',views.approve_seller),
    path('home',views.admin_home),
    path('login',views.admin_login),
    path('viewcustomer',views.view_customer),
    path('viewseller',views.view_seller),
    path('sellerorder',views.seller_order)
]