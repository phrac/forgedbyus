# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20151013_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='parallax_blurb',
            field=models.TextField(null=True),
        ),
    ]
