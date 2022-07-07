from django.shortcuts import render

def shop_index(request):
    return render(request, "front/pages/index.html")

def shop_detail_product(request):
    return render(request, "front/pages/single-product-details.html")

def shop_list_product(request):
    return render(request, "front/pages/index.html")

def shop_checkout(request):
    return render(request, "front/pages/checkout.html")



