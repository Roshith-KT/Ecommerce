from django.shortcuts import render
from credentials.models import Profile
from wholeshopview.models import Product
from orders.models import Order,OrderItem
# Create your views here.

def ecomadmin_dash(request):
    customer_count=Profile.objects.all().count()
    product_count=Product.objects.all().count()
    order_count=Order.objects.all().count()
    context={
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count
    }
    return render(request,'ecomadmin/ecomadmin_dash.html',context)


def products(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'ecomadmin/products.html',context)


def orders(request):
    orders=OrderItem.objects.all()
    context={
        'orders':orders
    }
    return render(request,'ecomadmin/orders.html',context)


def customers(request):
    customers=Profile.objects.all()
    context={
        'customers':customers
    }
    return render(request,'ecomadmin/customers.html',context)