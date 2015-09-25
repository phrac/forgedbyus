# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150925_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='affiliated_id',
            new_name='affiliate_id',
        ),
    ]
