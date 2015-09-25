# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_amazon_prime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='current_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(unique=True, max_length=13, blank=True),
        ),
    ]
