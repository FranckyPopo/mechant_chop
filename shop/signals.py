from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

import random

from shop import models


@receiver(pre_save, sender=models.Product)
def generator_slug(instance: models.Product, **kwargs) -> None:
    """Cette fonction a pour mission de générer un slug valide  
    
    Args:
        instance (Product): L'instance models.Product qui s'apprête a être enregistré
    """
    
    if not instance.slug:
        instance.slug = f"{slugify(instance.name)}"