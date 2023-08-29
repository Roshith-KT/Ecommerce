from django import forms
from orders.models import OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderItem
        fields=['status']