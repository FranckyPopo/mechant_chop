from django.template.loader import render_to_string

from shop import models, utils


def list_category(request):
    return {"categories": models.Category.objects.all().filter(active=True)}


def list_product(request):
    return {"products": models.Product.objects.all().filter(active=True)}


def get_total_product_quantity(request):
    cart = request.session.get("cart", [])
    total_product_quantity = sum([order["quantity"] for order in cart])
    
    return {
        "total_product": total_product_quantity
    }

    
def total_price_cart(request):
    return {
        "total_price_cart": None
    }
    

def cart(request):
    context = {"cart": utils.get_cart_product(request)}
    cart = render_to_string("shop/pages/cart-list.html", context=context)
    return {"cart": cart}
    
