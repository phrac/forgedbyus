# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(unique=True, max_length=13)),
                ('title', models.CharField(max_length=64)),
                ('asin', models.CharField(max_length=10, unique=True, null=True, blank=True)),
                ('brand', models.CharField(max_length=128, null=True)),
                ('manufacturer', models.CharField(max_length=128, null=True)),
                ('state_of_origin', models.CharField(max_length=2, null=True, blank=True)),
                ('usa_verified', models.BooleanField(default=False)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('current_price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('avg_rating', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('thumb', models.ImageField(upload_to=b'')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
