# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20151006_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='image',
        ),
        migrations.AddField(
            model_name='collection',
            name='banner',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collection',
            name='parallax',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='story',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
