from django.shortcuts import render,redirect
from wholeshopview.models import Product
from django.contrib.auth.decorators import login_required
from . models import Cart,CartItem
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='credentials:login')
def cart_view(request):
    try:
        cart=Cart.objects.get(user=request.user)
        cart.grand_total=0
        cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            user=request.user
        )
        
    
    cart_items=CartItem.objects.all().filter(cart=cart)
        
    for i in cart_items:
        cart.grand_total += i.total
    cart.save()
    
    
    return render(request,'cart/cart_view.html',{'cart_items':cart_items,'cart':cart})


# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

def add_to_cart(request,id):
    product=Product.objects.get(id=id)

    try:
        cart=Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            user=request.user
        )
        cart.save()
    
    try:
        cart_item=CartItem.objects.get(cart=cart,product=product)
        cart_item.quantity += 1
        cart_item.total += cart_item.product.price
        cart_item.save()


    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=1,
            total=product.price
        )
        cart_item.save()
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('cart:cart_view')

def cartitem_remove(request,id):
    cart_item=CartItem.objects.get(id=id)
    if cart_item.quantity==1:
        cart_item.delete()
    else:
        cart_item.quantity -=1
        cart_item.total -=cart_item.product.price
        cart_item.save()
    return redirect('cart:cart_view')


def cartitem_delete(request,id):
    cart_item=CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect('cart:cart_view')
    