from django.urls import path
from . import views

app_name="cart"

urlpatterns=[
    path('cart_view',views.cart_view,name='cart_view'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('cartitem_remove/<int:id>',views.cartitem_remove,name='cartitem_remove'),
    path('cartitem_delete/<int:id>',views.cartitem_delete,name='cartitem_delete'),
    path('checkout',views.checkout,name='checkout'),
]