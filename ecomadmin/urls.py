from django.urls import path
from . import views

app_name='ecomadmin'

urlpatterns =[
    path('ecomadmin_dash',views.ecomadmin_dash,name='ecomadmin_dash'),
]