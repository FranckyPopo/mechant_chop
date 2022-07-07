from django.contrib import admin
from django.urls import path

from shop import views
from front.views import front_contact 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shop_index, name="shop_index"),
    path('detail-product/', views.shop_detail_product, name="shop_detail_product"),
    path('list-product/', views.shop_list_product, name="shop_list_product"),
    path('checkout/', views.shop_checkout, name="shop_checkout"),
    path('contact/', front_contact, name="shop_contact"),
]
