from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class SiteInfo(models.Model):
    phone = PhoneNumberField(region="CI")
    email = models.EmailField()
    address = models.CharField(max_length=150) 
    message = models.CharField(max_length=150) 
    copyright_  = models.CharField(max_length=150, verbose="copyright") 
    
    link_facebook = models.URLField(blank=True)
    link_instagram = models.URLField(blank=True)
    link_twitter = models.URLField(blank=True)
    link_youtube = models.URLField(blank=True)
    link_pinterest = models.URLField(blank=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    