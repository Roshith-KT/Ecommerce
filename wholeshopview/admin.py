from django.contrib import admin
from . models import Category,Product,Type

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Type)