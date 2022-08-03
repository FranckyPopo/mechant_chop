from django.db import models
from colorfield.fields import ColorField
from django.conf import settings

from pprint import pprint

class Brand(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    active = models.BooleanField(default=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=150) 
    active = models.BooleanField(default=True)
    image = models.ImageField()
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class GlobalSold(models.Model):
    name = models.PositiveIntegerField(blank=True, null=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Size(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=150)
    code = ColorField()
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150) 
    description = models.CharField(max_length=1000)
    first_photo = models.ImageField()
    second_photo = models.ImageField()

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="product_brand")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="product_size")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="product_color")

    price = models.PositiveIntegerField(default=0)
    promotion_percentage = models.PositiveIntegerField(blank=True, null=True)
    promotion_price = models.PositiveIntegerField(blank=True, null=True)

    like = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Cart
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.product} ({self.quantity})"
    
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username

class ImageProduct(models.Model):
    image = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image_product")

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
        
class NewsLater(models.Model):
    email = models.EmailField(unique=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
