from shop.models import OrderItem
from django.db.models import Sum


def details_cart(session_id) -> int:
    s = OrderItem.objects.filter(
        session_id=session_id
    )
    return s.aggregate(Sum("quantity"))['quantity__sum']

