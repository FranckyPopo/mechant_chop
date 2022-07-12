from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string

import json

from shop import models, utils

class Cart(View):
    template_name = "shop/pages/index.html"
    
    def post(self, request):
        product_pk = int(request.POST.get("pk"))
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
        response = render_to_string("shop/pages/cart-list.html", context={"cart": cart})
        
        return HttpResponse(
            response,
            headers={
                "HX-Trigger": json.dumps({
                    "porduct_add": {
                        "total_product": utils.sum_quantity_cart(session_id)
                    }
                })
            }
        )


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
