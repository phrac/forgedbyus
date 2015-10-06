# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20151005_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
