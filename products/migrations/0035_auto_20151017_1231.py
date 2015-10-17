# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20151017_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collections',
            field=models.ManyToManyField(to='products.Collection', blank=True),
        ),
    ]
