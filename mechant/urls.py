from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from shop import views
from front.views import front_contact 
from authentication.views import LoginView

urlpatterns = [
    # Authentication
    path("login/", LoginView.as_view(), name="authentication_login"),
     
    path('admin/', admin.site.urls),
    path('', views.shop_index, name="shop_index"),
    path('detail-product/', views.shop_detail_product, name="shop_detail_product"),
    path('list-product/', views.shop_list_product, name="shop_list_product"),
    path('checkout/', views.shop_checkout, name="shop_checkout"),
    path('contact/', front_contact, name="shop_contact"),
    
    
    
    path('product-add-cart/<int:product_pk>/', views.ProductAddCart.as_view(), name="shop_add_product_cart"),
    path('product-delete-cart/<int:product_pk>/', csrf_exempt(views.ProductDeleteCart.as_view()), name="shop_delete_product_cart"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
