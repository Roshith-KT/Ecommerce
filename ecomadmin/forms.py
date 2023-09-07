from django import forms
from orders.models import OrderItem
from credentials.models import Profile
from wholeshopview.models import Product
from . models import Store_Address
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderItem
        fields=['status']
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['mobile','address','is_email_verified','profile_image']
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','type','price','description','image']
        
        
class StoreAddressForm(forms.ModelForm):
    class Meta:
        model=Store_Address
        fields=[
            'store_location',
            'work_hours',
            'phone',
            'email',
            'office_location',
        ]
        
        