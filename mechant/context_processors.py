from shop import models, utils


def list_category(request):
    return {"categories": models.Category.objects.all().filter(active=True)}


def list_product(request):
    return {"products": models.Product.objects.all().filter(active=True)}


def total_product(request):
    return {
        "total_product": utils.sum_quantity_cart(request.session._get_or_create_session_key()),
    }


def total_price(request):
    return {"tota_price_cart": utils.tota_price_cart()} 
