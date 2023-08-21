from django.urls import path
from . import views

app_name='orders'

urlpatterns=[
    path('checkout',views.checkout,name='checkout'),
    path('orders_view',views.orders_view,name='orders_view'),
    path('order_tracking',views.order_tracking,name='order_tracking'),
    path('order_detail/<int:id>',views.order_detail,name='order_detail'),
    path('tracked_order/<str:tracking_id>',views.tracked_order,name='tracked_order'),
    path('payment_success',views.payment_success,name='payment_success'),
    path('payment_failure',views.payment_failure,name='payment_failure'),
]