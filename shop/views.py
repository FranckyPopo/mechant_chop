from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string

import json

from shop import models
from mechant import context_processors

class ProductAddCart(View):
    http_method_names = ["post"]
    template_name = "shop/pages/cart-list.html"
    
    def post(self, request, product_pk):
        if request.user.is_authenticated:
            pass
        else:
            self.add_to_cart_session(request, int(product_pk))
            total_product_quantity = context_processors.get_total_product_quantity(request)
        
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "product_add": {
                        "total_product": total_product_quantity["total_product"],
                        "tota_price_cart": None,
                    }
                })
            }
        )
    
    def add_to_cart_session(self, request, product_pk: int) -> None:
        """Cette méthode va permtre d'ajouter des produits
        dans un panier via la session de l'utilisateur"""
        
        if not request.session.session_key: request.session.save()
        quantity = request.POST.get("quantity", False)
        cart = request.session.get("cart", False)
            
        if quantity:
            for order in cart:
                if order["pk"] == product_pk:
                    order["quantity"] = int(quantity)
                    request.session["cart"] = cart
                    break
        elif cart:
            for order in cart:
                if order["pk"] == product_pk:
                    order["quantity"] += 1
                    request.session["cart"] = cart
                    break
            else:
                order = {
                    "pk": product_pk,
                    "quantity": 1
                }
                cart.append(order)
                request.session["cart"] = cart
        elif not cart:
            request.session["cart"] = [
                {"pk": product_pk, "quantity": 1}
            ]
        print(cart)

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

    context = {
        "cart": None,
    }
    
    return render(request, "shop/pages/index.html", context=context)

def shop_detail_product(request):
    return render(request, "shop/pages/single-product-details.html")

def shop_list_product(request):
    return render(request, "shop/pages/shop.html")

def shop_checkout(request):
    return render(request, "shop/pages/checkout.html")
