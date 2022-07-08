from django.contrib import admin

from shop import models

@admin.register(models.Brand)
class Brand(admin.ModelAdmin):
    list_display = ["name", "active", "date_create", "date_update"]
    
@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ["name", "active", "date_create", "date_update"]
    
@admin.register(models.GlobalSold)
class GlobalSold(admin.ModelAdmin):
    list_display = ["name", "description", "date_create", "date_update"]
    
@admin.register(models.Size)
class Size(admin.ModelAdmin):
    list_display = ["name", "active", "date_create", "date_update"]
    
@admin.register(models.Color)
class Color(admin.ModelAdmin):
    list_display = ["name", "code", "active", "date_create", "date_update"]
    
@admin.register(models.Product)
class Product(admin.ModelAdmin):
    list_display = ["name", "brand", "date_create", "date_update"]
    
@admin.register(models.ImageProduct)
class ImageProduct(admin.ModelAdmin):
    list_display = ["image", "date_create", "date_update"]
    
@admin.register(models.NewsLater)
class NewsLater(admin.ModelAdmin):
    list_display = ["email", "date_create", "date_update"]
