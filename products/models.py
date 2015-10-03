from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from localflavor.us.models import USStateField
from localflavor.us.us_states import US_STATES
from django.db import models

from affiliates.models import Affiliate
from brands.models import Brand

import random
import string

def id_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        pass


class Product(models.Model):
    product_id = models.CharField(db_index=True, max_length=13, unique=True, blank=True)
    affiliate = models.ForeignKey(Affiliate)
    title = models.CharField(max_length=256)
    asin = models.CharField(max_length=10, null=True, blank=True)
    brand = models.ForeignKey(Brand)
    manufacturer = models.CharField(max_length=128, null=True, blank=True)
    state_of_origin = USStateField(blank=True)
    usa_verified = models.BooleanField(default=False)
    short_description = models.TextField()
    description = models.TextField(null=True, blank=True)
    msrp = models.IntegerField(null=True, blank=True)
    current_price = models.IntegerField()
    detail_views = models.IntegerField(default=0)
    amazon_prime = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    curated = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)
    sales_rank = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True)
    features = ArrayField(
        models.CharField(max_length=128, null=True, blank=True),
        null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = id_generator()
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_amazon_url(self):
        if self.asin:
            return "http://www.amazon.com/dp/%s/?tag=%s" % (self.asin, settings.AWS_ASSOCIATE_TAG)
        else:
            return None

    def get_full_state(self):
        if self.state_of_origin:
            return [x[1] for x in US_STATES if x[0] == self.state_of_origin][0].upper()
        else:
            return None

    @models.permalink
    def get_absolute_url(self):
        return ('products.views.details', [self.product_id])

class Collection(models.Model):
    name = models.CharField(max_length=32, unique=True)
    products = models.ManyToManyField(Product)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
