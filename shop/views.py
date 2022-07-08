from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string

import json

from shop import models

class Cart(View):
    template_name = "shop/pages/index.html"
    
    def post(self, request):
        # Récpération du pk du produit ajouter dans le panier
        product_pk = int(request.POST.get("pk"))
        session_id = request.session._get_or_create_session_key()
        quantity = 1
        product = models.Product.objects.get(pk=product_pk)
        
        # Création du panier de l'utilisateur
        models.OrderItem.objects.create(
            session_id=session_id, 
            product=product, 
            quantity=quantity
        )
        
        cart = models.OrderItem.objects.filter(session_id=session_id)
        r = render_to_string("shop/pages/cart-list.html", context={"cart": cart})
                
        return HttpResponse(r)

def shop_index(request):
    session_id = request.session._get_or_create_session_key()
    cart = models.OrderItem.objects.filter(session_id=session_id)
    data = {
        "cart": cart,
    }
    
    
    return render(request, "shop/pages/index.html", context=data)

def shop_detail_product(request):
    return render(request, "shop/pages/single-product-details.html")

def shop_list_product(request):
    return render(request, "shop/pages/shop.html")

def shop_checkout(request):
    return render(request, "shop/pages/checkout.html")
