from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

import random

from shop import models


@receiver(pre_save, sender=models.Product)
def generator_slug(instance: models.Product, **kwargs) -> None:
    """
    Cette fonction a pour mission de générer un slug valide  
    
    Args:
        instance (Product): L'instance models.Product qui s'apprête a être enregistré
    """
    
    if not instance.slug:
        instance.slug = f"{slugify(instance.name)}"
        
        
@receiver(post_save, sender=models.Product)
def active_category_and_sub_category(instance: models.Product, **kwargs):
    """
    Cette fonction a pour mission d'activer la catégorie et
    la sous catégorie qui est relié au produit
    
    Args:
        instance (models.Product): instance  qui a été enregistré
    """
    
    category = instance.sub_category.category
    sub_category = instance.sub_category
    
    if not category.active and not sub_category.active:
        category.active = True
        category.save()
        sub_category.active = True
        sub_category.save()
      
        
@receiver(post_save, sender=models.SubCategory)
def active_category(instance: models.SubCategory, **kwargs):
    """
    Cette fonction a pour mission d'activer une catégorie
    seulement si une (1) des sous catégories a un produit 
    qui lui est relié 

    Args:
        instance (models.SubCategory): instance qui a été
        enregistré
    """
    
    category = instance.category
    sub_categories = category.sub_category.filter(active=True)
    
    for sub_category in sub_categories:
        if sub_category.product_sub_category.all():
            category.active = True
            break
    else:
        category.active = False
    category.save()
        
