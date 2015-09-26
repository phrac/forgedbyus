# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('products', '0012_remove_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, to='brands.Brand'),
            preserve_default=False,
        ),
    ]
