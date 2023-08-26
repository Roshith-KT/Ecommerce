from django.shortcuts import render
from credentials.models import Profile
from wholeshopview.models import Product
from orders.models import Order
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

