# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_collection_parallax_blurb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ManyToManyField(to='products.Collection', null=True, blank=True),
        ),
    ]
