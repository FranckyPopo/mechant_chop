from django.contrib import admin
from django.urls import path

from shop import views
from front import front_contact 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shop_index),
    path('detail-product/', views.shop_detail_product),
    path('list-product/', views.shop_list_product),
    path('checkout/', views.shop_checkout),
    path('contact/', views.front_contact),
]
