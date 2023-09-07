from django.db import models

# Create your models here.
class Contact_Us(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.TextField(max_length=5000)
    
    
    def __str__(self):
        return 'message from {}'.format(self.name)
    
    
    
class Store_Address(models.Model):
    store_name=models.CharField(max_length=255)
    store_location=models.CharField(max_length=255)
    work_hours=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.CharField(max_length=255)
    office_location=models.CharField(max_length=255)
    
    def __str__(self):
        return '{}'.format(self.store_name)
