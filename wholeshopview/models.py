from django.db import models
from django.utils.text import slugify


# Models created
class Type(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True,blank=True)
    description=models.TextField(max_length=2500,blank=True)
    image=models.ImageField(upload_to='type_images')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True,blank=True)
    description=models.TextField(max_length=2500,blank=True)
    image=models.ImageField(upload_to='category_images')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,blank=True,null=True)
    price=models.IntegerField()
    description=models.TextField(max_length=2500,blank=True)
    image=models.ImageField(upload_to='product_images')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    


#By Roshith.K.T