from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name ="credentials"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('activate/<email_token>',views.activate_account,name='activate_account'),
    path('password_reset',views.password_reset, name='password_reset'),
    path('password_reset_page/<str:email>',views.password_reset_page, name='password_reset_page'),
    
    path('adminlogin', LoginView.as_view(template_name='ecomadmin/admin_login.html'),name='adminlogin'),
    path('adminlogout', LogoutView.as_view(template_name='ecomadmin/admin_logout.html'),name='adminlogout'),
   
]
