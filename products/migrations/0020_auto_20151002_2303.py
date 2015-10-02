# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0019_product_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_features',
        ),
        migrations.AddField(
            model_name='product',
            name='curated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
