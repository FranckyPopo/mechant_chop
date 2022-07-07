from django.shortcuts import render

def shop_index(request):
    return render(request, "shop/pages/index.html")

def shop_detail_product(request):
    return render(request, "shop/pages/single-product-details.html")

def shop_list_product(request):
    return render(request, "shop/pages/shop.html")

def shop_checkout(request):
    return render(request, "shop/pages/checkout.html")
