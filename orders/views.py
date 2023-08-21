from django.shortcuts import render,redirect
from cart.models import Cart,CartItem
from . models import Order,OrderItem
import random
# Create your views here.
def checkout(request):
    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        country=request.POST['country']
        mobile=request.POST['mobile']
        email=request.POST['email']
        
        cart=Cart.objects.get(user=request.user)
        cartitems=CartItem.objects.all().filter(cart=cart)

        try:
            order=Order.objects.get(user=request.user)
        except Order.DoesNotExist:
            order=Order.objects.create(user=request.user)


        for i in cartitems:
            orderitem=OrderItem.objects.create(
                order=order,
                product=i.product.name,
                quantity=i.quantity,
                price=i.total,
                name=name,
                address=address,
                district=district,
                state=state,
                country=country,
                mobile=mobile,
                email=email,
                image=i.product.image,
                tracking_id=random.randint(1000000,9999999)
            )
            orderitem.save()
        cart.delete()
        return redirect('orders:payment_success')
    return render(request,'orders/checkout.html')


def orders_view(request):
    user=request.user
    order=Order.objects.get(user=user)
    order_items=OrderItem.objects.all().filter(order=order).order_by('-created_at')
    return render(request,'orders/orders_view.html',{'order_items':order_items})

def order_detail(request,id):
    order_item=OrderItem.objects.get(id=id)
    context={
        "order_item":order_item
    }
    return render(request,'orders/order_detail.html',context)

def order_tracking(request):
    if request.method=='POST':
        tracking_id=request.POST['tracking_id']
        return redirect('orders:tracked_order',tracking_id=tracking_id)
    return render(request,'orders/ordertracking.html')

def tracked_order(request,tracking_id):
    try:
        order_item=OrderItem.objects.get(tracking_id=tracking_id)
    except OrderItem.DoesNotExist:
        order_item=None
    context={
            "order_item": order_item
        }
    return render(request,'orders/tracked_order.html',context)


def payment_success(request):
    return render(request,'orders/success.html')

def payment_failure(request):
    return render(request,'orders/failure.html')