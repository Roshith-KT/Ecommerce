from django.db import models
from wholeshopview.models import Product


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    grand_total=models.IntegerField(default=0)

    class Meta:
        db_table = 'Cart'


    def __str__(self):
        return '{}'.format(self.cart_id)
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total=models.IntegerField()

    class Meta:
        db_table = 'CartItem'

    
    def __str__(self):
        return '{}'.format(self.product)

