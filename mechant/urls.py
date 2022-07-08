from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop import views
from front.views import front_contact 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shop_index, name="shop_index"),
    path('detail-product/', views.shop_detail_product, name="shop_detail_product"),
    path('list-product/', views.shop_list_product, name="shop_list_product"),
    path('checkout/', views.shop_checkout, name="shop_checkout"),
    path('contact/', front_contact, name="shop_contact"),
    path('cart/', views.Cart.as_view(), name="shop_cart"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
