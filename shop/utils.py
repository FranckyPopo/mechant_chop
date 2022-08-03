from shop import models


def add_to_cart_session(request, product_pk: int) -> None:
    """Cette fonction va permtre d'ajouter des produits
    dans un panier via la session de l'utilisateur"""
    
    if not request.session.session_key: request.session.save()
    quantity = request.POST.get("quantity", False)
    cart = request.session.get("cart", False)
        
    if quantity:
        for order in cart:
            if order["pk"] == product_pk:
                order["quantity"] = int(quantity)
                request.session["cart"] = cart
                break
    elif cart:
        for order in cart:
            if order["pk"] == product_pk:
                order["quantity"] += 1
                request.session["cart"] = cart
                break
        else:
            order = {
                "pk": product_pk,
                "quantity": 1
            }
            cart.append(order)
            request.session["cart"] = cart
    elif not cart:
        request.session["cart"] = [
            {"pk": product_pk, "quantity": 1}
        ]

def get_cart_product(request) -> [dict]:
    """Cette fonction va retourner une liste qui contiendra des
    disctionnaires qui aurons les clés suivante: product et quantity."""
    
    cart_session = request.session.get("cart", [])
    cart = []
    for order in cart_session:
        instance = {
            "product": models.Product.objects.get(pk=order["pk"]),
            "quantity": order["quantity"],
        }
        cart.append(instance)        
    return cart
