from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True,unique='True')
    profile_image=models.ImageField(upload_to='profile_image',default='noImage.png')
    mobile=models.IntegerField(blank=True,null=True,unique='True')
    address=models.TextField(blank=True,null=True,max_length=255)
    
    def __str__(self):
        return self.user.username