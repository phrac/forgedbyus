# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20151004_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 23, 21, 13, 807520, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
