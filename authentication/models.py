from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    MAN = "M"
    WOMEN = "F"
    choice_genre = [
        (MAN, "Homme"),
        (WOMEN, "Femme"),
    ] 
    
    phone = PhoneNumberField(region="CI")
    genre = models.CharField(max_length=2, choices=choice_genre)
    newslater = models.BooleanField(default=False)