# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20151002_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=128, null=True, blank=True), blank=True),
        ),
    ]
