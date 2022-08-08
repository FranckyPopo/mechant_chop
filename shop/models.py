from django.db import models
from colorfield.fields import ColorField
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

class Brand(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    active = models.BooleanField(default=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=150) 
    active = models.BooleanField(default=True)
    image = models.ImageField()
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class GlobalSold(models.Model):
    name = models.PositiveIntegerField(blank=True, null=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Size(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=150)
    code = ColorField()
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150) 
    description = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True)
    first_photo = models.ImageField()
    second_photo = models.ImageField()

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="product_brand")
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)

    price = models.PositiveIntegerField(default=0)
    is_promotion = models.BooleanField(default=False)
    promotion_percentage = models.PositiveIntegerField(blank=True, null=True)
    promotion_price = models.PositiveIntegerField(blank=True, null=True)

    like = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_price_promotion(self) -> int:
        """Cette méthode retourne le prix d'un article aprés
        déduction de la promotion s'il en a, dans le cas contraire
        retourne le prix original de l'article

        Returns:
            int : le prix finale de l'article
        """
        if self.is_promotion:
            if self.promotion_percentage:
                return {
                    "price_promotion": self.price * self.promotion_percentage // 100,
                    "reduction": self.promotion_percentage,
                    "symbole": "%"
                } 
            else:
                return {
                    "price_promotion": self.price - self.promotion_price,
                    "reduction": self.promotion_price,
                    "symbole": "XOF"
                } 
        return self.price
    
    def is_new(self) -> bool:
        pass

# Cart
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.product} ({self.quantity})"
    
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username

    @classmethod
    def add_cart_session_bd(cls, request) -> None:
        """Cette méthode va permetre d'ajouter le pannier qui se
        trouve dans la session de l'utilisateur dans le model Cart"""
        
        cart_session = request.session.get("cart", [])
        user = request.user
        cart, _ = cls.objects.get_or_create(user=user, ordered=False)
        
        for order_session in cart_session:
            product = Product.objects.get(pk=order_session["pk"])
            order, create = Order.objects.get_or_create(
                user=user,
                product=product,
                ordered=False
            )
            
            if create:
                order.quantity = order_session["quantity"]
                order.save()
                cart.order.add(order)
                cart.save()
            else:
                order.quantity += order_session["quantity"]
                order.save()

    @classmethod
    def add_to_cart(cls, request, product_pk: int) -> None:
        """Cette méthode va permetre d'ajouter des produits dans
        le panier de l'utilisateur quand il est connecté"""

        user = request.user
        size_pk = request.POST.get("size", False)
        color_pk = request.POST.get("color", False)
        product = get_object_or_404(Product, pk=product_pk)
        cart = cls.objects.get(user=user, ordered=False)
        
        if size_pk and color_pk:
            size = get_object_or_404(Size, pk=int(size_pk))
            color = get_object_or_404(Color, pk=int(color_pk))
            order, create = Order.objects.get_or_create(
                user=user,
                product=product,
                size=size,
                color=color,
                ordered=False
            )
        else:
            defaul_size = product.size.get(name="XL")
            defaul_color = product.color.get(name="White")
            order, create = Order.objects.get_or_create(
                user=user,
                product=product,
                size=defaul_size,
                color=defaul_color,
                ordered=False
            )
            
        if create:
            cart.order.add(order)
            cart.save()
        else:
            order.quantity += 1
            order.save()

    @classmethod
    def delete_to_cart(cls, request: HttpRequest, product_pk: int, color_pk: int, size_pk: int) -> None:
        """Cette méthode va permetre de supprimer un produit dans
        le panier de l'utilisateur quand il est connecté"""
        
        user = request.user
        cart = cls.objects.get(user=user, ordered=False)
        orders = cart.order.get(
            product__pk=product_pk,
            color__pk=color_pk,
            size__pk=size_pk
        )
        orders.delete()
    
class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image_product")
    image = models.ImageField()

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
        
class NewsLater(models.Model):
    email = models.EmailField(unique=True)
    
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
