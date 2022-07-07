from django.db import models
from colorfield.fields import ColorField


class Brand(models.Model):
    name = models.CharField(max_length=150)
    image = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
class Category(models.Model):
    name = models.CharField(max_length=150) 
    active = models.BooleanField(default=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
class GlobalSold(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    promotion_percentage = models.PositiveIntegerField(blank=True, null=True)
    promotion_price = models.PositiveIntegerField(blank=True, null=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
class Size(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
class Color(models.Model):
    name = models.CharField(max_length=150)
    code = ColorField()
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
class Product(models.Model):
    name = models.CharField(max_length=150) 
    description = models.CharField(max_length=1000)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    price = models.PositiveIntegerField(default=0)
    promotion_percentage = models.PositiveIntegerField(blank=True, null=True)
    promotion_price = models.PositiveIntegerField(blank=True, null=True)

    like = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)

class ImageProduct(models.Model):
    image = models.ForeignKey(Product, on_delete=models.CASCADE)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
        
class NewsLater(models.Model):
    email = models.EmailField(unique=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    