from shop import models


def list_category(request):
    return {"categories": models.Category.objects.all().filter(active=True)}


def list_product(request):
    return {"products": models.Product.objects.all().filter(active=True)}


def get_total_product_quantity(request):
    cart = request.session.get("cart", False)
    total_product_quantity = sum([order["quantity"] for order in cart])
    
    return {
        "total_product": total_product_quantity
    }

    
def total_price_cart(request):
    return {
        "total_price_cart": None
    }


