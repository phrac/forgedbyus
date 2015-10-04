# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20151003_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
