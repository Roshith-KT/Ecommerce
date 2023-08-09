from django.shortcuts import render,redirect
from cart.models import Cart,CartItem
from . models import Order,OrderItem
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
                image=i.product.image
            )
            orderitem.save()
        cart.delete()
        return redirect('/')
    return render(request,'orders/checkout.html')


def orders_view(request):
    user=request.user
    order=Order.objects.get(user=user)
    order_items=OrderItem.objects.all().filter(order=order).order_by('-created_at')
    return render(request,'orders/orders_view.html',{'order_items':order_items})