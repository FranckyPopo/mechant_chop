from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.conf import settings

from shop import models
from authentication import forms

# Create your views here.
class LoginView(View):
    template_name = "authentication/login.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(
            username=username,
            password=password
        )
        
        if user:
            # auto-login user
            login(request, user)
            models.Cart.add_cart_session_bd(request)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return redirect("authentication_login")        
        
class SignUpView(View):
    template_name = "authentication/sign_up.html"
    form_class = forms.SignupForm
    
    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect("authentication_login")
        return render(request, self.template_name, context={"form": form})
        
        