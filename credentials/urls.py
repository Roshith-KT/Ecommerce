from django.urls import path
from . import views

app_name ="credentials"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('activate/<email_token>',views.activate_account,name='activate_account'),
    path('password_reset',views.password_reset, name='password_reset'),
    path('password_reset_page/<str:email>',views.password_reset_page, name='password_reset_page'),
   
]
