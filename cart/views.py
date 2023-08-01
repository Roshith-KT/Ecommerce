from django.shortcuts import render
from wholeshopview.models import Product

# Create your views here.
def cart_view(request):
    products=Product.objects.all()
    return render(request,'cart/cart_view.html',{'products':products})