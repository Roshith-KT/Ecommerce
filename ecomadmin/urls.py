from django.urls import path
from . import views

app_name='ecomadmin'

urlpatterns =[
    path('ecomadmin_dash',views.ecomadmin_dash,name='ecomadmin_dash'),
    path('products',views.products,name='products'),
    path('orders',views.orders,name='orders'),
    path('customers',views.customers,name='customers'),
    path('update_customer/<int:id>/',views.update_customer,name='update_customer'),
    path('delete_customer/<int:id>/',views.delete_customer,name='delete_customer'),
    path('update_order/<int:id>/',views.update_order,name='update_order'),
    path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
    path('add_product',views.add_product,name='add_product'),
    path('customer_to_admin_messages',views.customer_to_admin_messages,name='customer_to_admin_messages'),
    path('update_store_details',views.update_store_details,name='update_store_details')
]