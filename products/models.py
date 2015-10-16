from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from localflavor.us.models import USStateField
from localflavor.us.us_states import US_STATES
from django.db import models

from affiliates.models import Affiliate
from brands.models import Brand

from slugify import slugify as awesome_slugify

import math

def id_generator():
    import random
    import string
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = awesome_slugify(self.name, max_length=settings.SLUG_MAX_LENGTH, to_lower=True)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'category', (), {'slug': self.slug}



class Product(models.Model):
    product_id = models.CharField(db_index=True, max_length=13, unique=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    affiliate = models.ForeignKey(Affiliate)
    title = models.CharField(max_length=256)
    asin = models.CharField(db_index=True, max_length=10, null=True, blank=True)
    brand = models.ForeignKey(Brand)
    manufacturer = models.CharField(max_length=128, null=True, blank=True)
    state_of_origin = USStateField(blank=True)
    usa_verified = models.BooleanField(default=False)
    short_description = models.TextField()
    description = models.TextField(null=True, blank=True)
    msrp = models.IntegerField(null=True, blank=True)
    current_price = models.IntegerField()
    price_updated = models.DateTimeField(auto_now_add=True)
    detail_views = models.IntegerField(default=0)
    amazon_prime = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    curated = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)
    thumb = models.ImageField(blank=True, null=True)
    sales_rank = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True)
    features = ArrayField(
        models.CharField(max_length=128, null=True, blank=True),
        null=True, blank=True
    )
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = id_generator()
        if not self.slug:
            self.slug = awesome_slugify(self.title, max_length=settings.SLUG_MAX_LENGTH, to_lower=True)
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
            return 'USA'

    def twitter_text(self):
        import urllib
        return urllib.quote_plus("%s by %s - Made in %s. #MadeInAmerica " % (self.title, self.brand, self.get_full_state()))

    @models.permalink
    def get_absolute_url(self):
        return 'product', (), {'product_id':self.product_id, 'slug': self.slug}

class Collection(models.Model):
    name = models.CharField(max_length=128, unique=True)
    story = models.TextField(null=True)
    products = models.ManyToManyField(Product, blank=True)
    parallax = models.ImageField(null=True, blank=True)
    banner = models.ImageField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = awesome_slugify(self.name, max_length=settings.SLUG_MAX_LENGTH, to_lower=True)
        super(Collection, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'collections', (), {'slug':self.slug}

    def __unicode__(self):
        return self.name
