from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json

from shop import models

class Cart(View):
    template_name = "shop/pages/index.html"
    
    def post(self, request):
        context = {}
        pk = int(request.POST.get("pk"))
        cart = request.COOKIES.get("cart")
        
        if cart:
            cart = cart.replace("\'", "\"")
            cart = json.loads(cart)
            
            # On Ajoute un 
            for item in cart:
                if item["pk"] == pk:
                    item["quantity"] += 1
                    break
                else:
                    product = {
                        "pk": pk,
                        "quantity": 1
                    }
                    cart.append(product)
                    break
        else:
            cart = [
               {
                   "pk": pk,
                   "quantity": 1
               } 
            ]
        context["cart"] = cart
        response = render(request, self.template_name, context=context)
        response.set_cookie(key="cart", value=json.dumps(cart))
        
        return response

def shop_index(request):
    cart = None
    if request.COOKIES.get("cart"):
        cart = json.loads(request.COOKIES.get("cart").replace("\'", "\""))
    data = {
        "brands": models.Brand.objects.all().filter(active=True),
        "cart": cart,
    }
    
    return render(request, "shop/pages/index.html", context=data)

def shop_detail_product(request):
    return render(request, "shop/pages/single-product-details.html")

def shop_list_product(request):
    return render(request, "shop/pages/shop.html")

def shop_checkout(request):
    return render(request, "shop/pages/checkout.html")
