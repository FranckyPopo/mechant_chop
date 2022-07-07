from shop import models


def list_category(request):
    return {"categories": models.Category.objects.all().filter(active=True)}


def list_product(request):
    return {"products": models.Product.objects.all().filter(active=True)}
