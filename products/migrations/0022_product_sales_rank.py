# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20151003_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales_rank',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
