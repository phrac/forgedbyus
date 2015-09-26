# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20150926_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='clicks',
            new_name='detail_views',
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 14, 22, 36, 848731, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
