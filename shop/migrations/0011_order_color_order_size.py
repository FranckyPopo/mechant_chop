# Generated by Django 4.0.6 on 2022-08-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_product_color_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='color',
            field=models.ManyToManyField(to='shop.color'),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.ManyToManyField(to='shop.size'),
        ),
    ]
