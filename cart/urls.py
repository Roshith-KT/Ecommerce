from django.urls import path
from . import views

app_name="cart"

urlpatterns=[
    path('cart_view',views.cart_view,name='cart_view'),
]