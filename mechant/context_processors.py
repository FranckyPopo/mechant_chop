from shop import models


def list_category(request):
    return {"categories": models.Category.objects.all().filter(active=True)}
