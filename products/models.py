from django.conf import settings
from localflavor.us.models import USStateField
from django.db import models

from affiliates.models import Affiliate
from brands.models import Brand

import random
import string

def id_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    parent_category = models.ForeignKey('Category', null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Product(models.Model):
    product_id = models.CharField(db_index=True, max_length=13, unique=True, blank=True)
    affiliate_id = models.ForeignKey(Affiliate)
    title = models.CharField(max_length=256)
    asin = models.CharField(max_length=10, null=True, blank=True)
    brand = models.ForeignKey(Brand)
    manufacturer = models.CharField(max_length=128, null=True)
    state_of_origin = USStateField()
    usa_verified = models.BooleanField(default=False)
    short_description = models.TextField()
    description = models.TextField(null=True)
    current_price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    amazon_prime = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = id_generator()
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_amazon_url(self):
        if self.asin:
            return "http://amazon.com/dp/%s/tag=%s" % (self.asin, settings.AWS_ASSOCIATE_TAG)
        else:
            return None

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    image = models.ImageField()
    thumb = models.ImageField()

class Collection(models.Model):
    name = models.CharField(max_length=32, unique=True)
    products = models.ManyToManyField(Product)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
