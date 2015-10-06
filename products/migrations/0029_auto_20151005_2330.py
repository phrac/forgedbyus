# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_product_price_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='asin',
            field=models.CharField(db_index=True, max_length=10, null=True, blank=True),
        ),
    ]
