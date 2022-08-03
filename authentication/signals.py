from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(user_logged_in)
def appu(sender, **kwargs):
    print("Connecté //////////////////////")


 











