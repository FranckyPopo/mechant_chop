from django.http import HttpRequest

from shop import models


def add_to_cart_session(request: HttpRequest, product_pk: int) -> None:
    """Cette fonction va permtre d'ajouter des produits
    dans un panier via la session de l'utilisateur"""
    
    if not request.session.session_key: request.session.save()
    
    quantity = request.POST.get("quantity", False)
    color_pk = request.POST.get("color", False)
    size_pk = request.POST.get("size", False)

    cart = request.session.get("cart", False)
        
    if quantity:
        for order in cart:
            if order["pk"] == product_pk:
                order["quantity"] = int(quantity)
                request.session["cart"] = cart
                break
    elif cart and color_pk and size_pk:
        color = models.Color.objects.get(pk=color_pk)
        size = models.Size.objects.get(pk=size_pk)
        for order in cart:
            # Vérifie qu'un produit existe avec les valeurs par default
            if (
                order["pk"] == product_pk
                and order["size"] == size.name 
                and order["color"] == color.name
            ):
                order["quantity"] += 1
                request.session["cart"] = cart
                break
        else:
            order = {
                "pk": product_pk,
                "quantity": 1,
                "size": size.name,
                "color": color.name
            }
            cart.append(order)
            request.session["cart"] = cart
    elif cart:
        for order in cart:
            # Vérifie qu'un produit existe avec les valeurs par default
            if (
                order["pk"] == product_pk
                and order["size"] == "XL" 
                and order["color"] == "White"
            ):
                order["quantity"] += 1
                request.session["cart"] = cart
                break
        else:
            order = {
                "pk": product_pk,
                "quantity": 1,
                "size": "XL",
                "color": "White",
            }
            cart.append(order)
            request.session["cart"] = cart
    elif not cart and color_pk and size_pk:
        color = models.Color.objects.get(pk=color_pk)
        size = models.Size.objects.get(pk=size_pk)
        request.session["cart"] = [
            {
                "pk": product_pk,
                "quantity": 1,
                "size": size.name,
                "color": color.name,
            }
        ]
    elif not cart:
        request.session["cart"] = [
            {
                "pk": product_pk,
                "quantity": 1,
                "size": "XL",
                "color": "White",
            }
        ]
        

def get_cart_product(request: HttpRequest) -> [dict]:
    """Cette fonction va retourner une liste qui contiendra des
    disctionnaires qui aurons les clés suivante: product et quantity."""
    
    cart_session = request.session.get("cart", [])
    cart = []
    for order in cart_session:
        instance = {
            "product": models.Product.objects.get(pk=order["pk"]),
            "quantity": order["quantity"],
            "color": models.Color.objects.get(name=order["color"]),
            "size": models.Size.objects.get(name=order["size"]),
        }
        cart.append(instance)        
    return cart
    
    
def delete_to_cart(request: HttpRequest, product_pk: int, color_pk: str, size_pk: str) -> None:
    cart = request.session.get("cart", [])
    color = models.Color.objects.get(pk=color_pk)
    size = models.Size.objects.get(pk=size_pk)
    
    for order in cart:
        
        if (
            order["pk"] == product_pk 
            and order["size"] == size.name 
            and order["color"] == color.name
        ):
            print(order["size"], order["color"])
            cart.remove(order)
            request.session["cart"] = cart
            break
        
        
