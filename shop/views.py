from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin

from typing import Any
import json

from shop import models, utils
from mechant import context_processors


class ProductAddCart(View):
    http_method_names = ["post"]
    template_name = "shop/pages/cart-list.html"
    
    def post(self, request, product_pk):        
        if request.user.is_authenticated:
            models.Cart.add_to_cart(request, int(product_pk))
            context = {"cart": models.Cart.objects.get(user=request.user, ordered=False)}
        else:
            utils.add_to_cart_session(request, int(product_pk))
            context = {"cart_session": utils.get_cart_product(request)}
        
        response = render_to_string(self.template_name, context=context)
        total_product_quantity = context_processors.get_total_product_quantity(request)
        
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
            models.Cart.delete_to_cart(request, int(product_pk))
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
    
        

    def http_method_not_allowed(self, request):
        return redirect("shop_index")

class FavouriteProuct(LoginRequiredMixin, View):
    
    def post(self, request: HttpRequest, product_pk: int) -> HttpResponse:
        """Cette méthode va permetre d'ajouter ou de retirer
        un produit des favoris

        Args:
            request (HttpRequest): Objet HttpRequest
            product_pk (int): pk du produit

        Returns:
            HttpResponse: réponse
        """
        
        product = get_object_or_404(models.Product, pk=product_pk)
        user = request.user
        likes = user.likes.all()
                
        for product_like in likes:
            if product_like == product:
                user.likes.remove(product_like)
                user.save()
                break
        else:
            user.likes.add(product)
            user.save()
        
        return HttpResponse("")
    
    def http_method_not_allowed(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return redirect("shop_index")
        
    
def shop_index(request):
    return render(request, "shop/pages/index.html")

def shop_detail_product(request):
    return render(request, "shop/pages/single-product-details.html")

def shop_list_product(request):
    return render(request, "shop/pages/shop.html")

def shop_checkout(request):
    return render(request, "shop/pages/checkout.html")
