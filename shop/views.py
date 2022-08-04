from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

import json

from shop import models, utils
from mechant import context_processors

class ProductAddCart(View):
    http_method_names = ["post"]
    template_name = "shop/pages/cart-list.html"
    
    def post(self, request, product_pk):
        if request.user.is_authenticated:
            pass
        else:
            utils.add_to_cart_session(request, int(product_pk))
            total_product_quantity = context_processors.get_total_product_quantity(request)
            context = {"cart": utils.get_cart_product(request)}
            response = render_to_string(self.template_name, context=context)
            
        return HttpResponse(
            response,
            headers={
                "HX-Trigger": json.dumps({
                    "product_add": {
                        "total_product": total_product_quantity["total_product"],
                        "tota_price_cart": None,
                    }
                })
            }
        )
    
    def http_method_not_allowed(self, request):
        
        return redirect("shop_index")
    
class ProductDeleteCart(View):
    http_method_names = ["post"]
    
    def post(self, request, product_pk=None):
        if request.user.is_authenticated:
            pass
        else:
            utils.delete_to_cart(request, int(product_pk))
            total_product_quantity = context_processors.get_total_product_quantity(request)
            
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "product_delete": {
                        "total_product": total_product_quantity["total_product"],
                        "tota_price_cart": None,
                    }
                })
            }
        )
        

    def http_method_not_allowed(self, request):
        return redirect("shop_index")

def shop_index(request):
    # session = Session.objects.get(session_key=request.session.session_key)
    print(dir(SessionStore))

    context = {
        "cart": None,
    }
    
    return render(request, "shop/pages/index.html")

def shop_detail_product(request):
    return render(request, "shop/pages/single-product-details.html")

def shop_list_product(request):
    return render(request, "shop/pages/shop.html")

def shop_checkout(request):
    return render(request, "shop/pages/checkout.html")
