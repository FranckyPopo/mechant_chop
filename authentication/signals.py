from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

def appu(sender, **kwargs):
    session_key = Session.objects.last()
    print(session_key)

    print("Connecté //////////////////////")


 











