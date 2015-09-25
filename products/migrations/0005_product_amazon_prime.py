# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150925_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amazon_prime',
            field=models.BooleanField(default=False),
        ),
    ]
