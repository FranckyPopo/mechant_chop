from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate

from shop import models

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
            login(request, user)
            models.Cart.add_cart_session_bd(request)
            return redirect("shop_index")
        return redirect("authentication_login")
        
        
        