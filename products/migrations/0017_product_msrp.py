# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20150926_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='msrp',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
