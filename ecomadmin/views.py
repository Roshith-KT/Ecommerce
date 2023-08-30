from django.shortcuts import render,redirect
from credentials.models import Profile
from wholeshopview.models import Product,Category,Type
from orders.models import Order,OrderItem
from django.contrib.auth.models import User
from . forms import UserForm,ProfileForm,OrderForm,ProductForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='credentials:adminlogin')
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

def edit_product(request,id):
    product=Product.objects.get(id=id)
    productform=ProductForm(request.FILES,instance=product)
    context={'productform':productform}
    if request.method=="POST":
        productform=ProductForm(request.POST,request.FILES,instance=product)
        if productform.is_valid():
            productform.save()
            return redirect('ecomadmin:products')
    return render(request,'ecomadmin/edit_product.html',context)

def add_product(request):
    categories=Category.objects.all()
    types=Type.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        type=request.POST['type']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['image']
        
        category_instance = Category.objects.get(name=category)
        type_instance = Type.objects.get(name=type)
        
        product=Product.objects.create(
            name=name,
            category=category_instance,
            type=type_instance,
            price=price,
            description=description,
            image=image
        )
        product.save()
        return redirect('ecomadmin:products')
    return render(request,'ecomadmin/add_product.html',{'categories':categories,'types':types})

def orders(request):
    orders=OrderItem.objects.all()
    context={
        'orders':orders
    }
    return render(request,'ecomadmin/orders.html',context)

def update_order(request,id):
    order=OrderItem.objects.get(id=id)
    orderform=OrderForm(request.FILES,instance=order)
    context={"orderform":orderform}
    if request.method=="POST":
        orderform=OrderForm(request.POST,request.FILES,instance=order)
        if orderform.is_valid():
            orderform.save()
            return redirect('ecomadmin:orders')
    return render(request,'ecomadmin/update_order.html',context)


def customers(request):
    customers=Profile.objects.all()
    context={
        'customers':customers
    }
    return render(request,'ecomadmin/customers.html',context)

def update_customer(request,id):
    user=User.objects.get(id=id)
    profile=Profile.objects.get(user=user)
    userform=UserForm(instance=user)
    profileform=ProfileForm(request.FILES,instance=profile)
    context={
        'userform':userform,
        'profileform':profileform
    }
    
    if request.method=='POST':
        userform=UserForm(request.POST,instance=user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return HttpResponseRedirect(request.path_info)
    return render(request,'ecomadmin/update_customer.html',context)


def delete_customer(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('ecomadmin:customers')
    