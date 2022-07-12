from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string

import json

from shop import models, utils

class ProductAddCart(View):
    http_method_names = ["post"]
    template_name = "shop/pages/cart-list.html"
    
    def post(self, request, product_pk):
        session_id = request.session._get_or_create_session_key()
        product = models.Product.objects.get(pk=product_pk)
        
        objet, created = models.OrderItem.objects.get_or_create(
            session_id=session_id,
            product=product,
        )     
        
        if not created:
            objet.quantity += 1
            objet.save()
                
        cart = models.OrderItem.objects.filter(session_id=session_id)
        response = render_to_string(self.template_name, context={"cart": cart})
        
        return HttpResponse(
            response,
            headers={
                "HX-Trigger": json.dumps({
                    "product_add": {
                        "total_product": utils.sum_quantity_cart(session_id),
                        "tota_price_cart": utils.sum_price_cart(session_id),
                    }
                })
            }
        )
    
    def http_method_not_allowed(self, request):
        return redirect("shop_index")
    
class ProductDeleteCart(View):
    http_method_names = ["post"]
    
    def post(self, request, product_pk):
        session_id = request.session._get_or_create_session_key()
        product = models.Product.objects.get(pk=product_pk)
        cart_delete = models.OrderItem.objects.get(product=product)
        cart_delete.delete()
        
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "product_delete": {
                        "total_product": utils.sum_quantity_cart(session_id),
                        "tota_price_cart": utils.sum_price_cart(session_id),
                    }
                })
            }
        )
        

    def http_method_not_allowed(self, request):
        return redirect("shop_index")

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
