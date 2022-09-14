from django.urls import path
from . import views


urlpatterns=[
    path('sellerhome',views.seller_home),
    path('sellercart',views.seller_cart),
    path('order',views.seller_order),
    path('addproduct',views.add_product),
    path('changepassword',views.change_password),
    path('stoke',views.stoke_update)
]