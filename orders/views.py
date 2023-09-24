from django.shortcuts import render,redirect
from cart.models import Cart,CartItem
from . models import Order,OrderItem
import random
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os 

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
    
    try:
        order=Order.objects.get(user=user)
    except Order.DoesNotExist:
        order=Order.objects.create(user=user)
        
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




def generate_invoice(request,id):
    try:
        order_item=OrderItem.objects.get(id=id)
        
    except OrderItem.DoesNotExist:
        return HttpResponse("505 Not Found")
    
    data={
        'product':order_item.product,
        'qty':order_item.quantity,
        'total':order_item.price,
        'name':order_item.name,
        'address':order_item.address,
        'district':order_item.district,
        'state':order_item.state,
        'country':order_item.country,
        'mobile':order_item.mobile,
        'email':order_item.email,
        'image':order_item.image,
        'tracking_id':order_item.tracking_id,
        'created_at':order_item.created_at,
        'taxable_amount':order_item.taxable_amount,
        'delivery_date':order_item.delivery_date,
        'tax_amount':order_item.tax_amount,
    }

    pdf=render_to_pdf("invoice/invoice.html", data)
    return HttpResponse(pdf,content_type='application/pdf')

    #force download pdf file code
    if pdf:
        response=HttpResponse(pdf,content_type='application/pdf')
        filename="Item_%s.pdf" %(data['item_name'])
        content="inline; filename='%s'" %(filename)
        content="attachment; filename=%s" %(filename)
        response['Content-Disposition']=content
        return response
    return HttpResponse("Not found")



def render_to_pdf(template_src,context_dict:dict):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)

    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None