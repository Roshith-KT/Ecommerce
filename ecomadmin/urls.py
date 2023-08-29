from django.urls import path
from . import views

app_name='ecomadmin'

urlpatterns =[
    path('ecomadmin_dash',views.ecomadmin_dash,name='ecomadmin_dash'),
    path('products',views.products,name='products'),
    path('orders',views.orders,name='orders'),
    path('customers',views.customers,name='customers'),
]