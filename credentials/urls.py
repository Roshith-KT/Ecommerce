from django.urls import path
from . import views

app_name ="credentials"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('activate/<email_token>',views.activate_account,name='activate_account'),
   
]
