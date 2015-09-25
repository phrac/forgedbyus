# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0001_initial'),
        ('products', '0002_auto_20150922_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='affiliated_id',
            field=models.ForeignKey(default=0, to='affiliates.Affiliate'),
            preserve_default=False,
        ),
    ]
