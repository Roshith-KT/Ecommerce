from django.urls import path
from . import views

app_name='orders'

urlpatterns=[
    path('checkout',views.checkout,name='checkout'),
    path('orders_view',views.orders_view,name='orders_view'),
]