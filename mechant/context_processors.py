from shop import models, utils


def list_category(request):
    return {"categories": models.Category.objects.all().filter(active=True)}


def list_product(request):
    return {"products": models.Product.objects.all().filter(active=True)}


def total_product(request):
    session_id = request.session._get_or_create_session_key()
    return {
        "total_product": utils.sum_quantity_cart(session_id)
    }

    
def total_price_cart(request):
    session_id = request.session._get_or_create_session_key()
    print("//////////", utils.sum_price_cart(session_id))
    return {
        "total_price_cart": utils.sum_price_cart(session_id)
    }


