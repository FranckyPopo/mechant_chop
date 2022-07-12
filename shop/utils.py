from django.db.models import Sum
from django.contrib.sessions.backends.db import SessionStore

from shop.models import OrderItem


s = SessionStore()
s.create()


print(s.session_key)

def sum_quantity_cart(session_id) -> int:
    s = OrderItem.objects.filter(
        session_id=session_id
    )
    return s.aggregate(Sum("quantity"))['quantity__sum'] or 0

def tota_price_cart() -> int:
    total_price = 5
    
    for item in OrderItem.objects.filter(session_id=SessionStore.session_key):
        quantity = item.quantity
        price = item.product.price
        total_price += quantity * price
        
    return total_price
