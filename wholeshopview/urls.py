from django.urls import path
from . import views

app_name="wholeshopview"

urlpatterns = [
    path('', views.home, name="home"),
    path('typeProductsView/<slug:slug>/',views.typeProductsView,name="typeProductsView"),
    path('singleProductView/<slug:slug>',views.singleProductView,name='singleProductView'),
    path('allProductsView/',views.allProductsView,name='allProductsView'),
    path('categoryProductView/<slug:slug>',views.categoryProductView,name="categoryProductView"),
]
