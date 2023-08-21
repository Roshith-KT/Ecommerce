from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
import uuid
# Create your models here.



class Order(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.user)
    

class OrderItem(models.Model):

    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    order=models.ForeignKey(Order,on_delete=models.CASCADE)

    product=models.CharField(max_length=255)
    quantity=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='order_images',null=True, blank=True)
    status=models.CharField(max_length=255,choices=STATUS,default='Pending')
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    mobile=models.IntegerField()
    email=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    tracking_id = models.IntegerField(unique=True,null=True,blank=True)

    def delivery_date(self):
        return self.created_at + timedelta(days=6)

    def __str__(self):
        return '{}'.format(self.product)
