# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20151013_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(to='products.Product', blank=True),
        ),
    ]
