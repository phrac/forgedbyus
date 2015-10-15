from amazon.api import AmazonAPI
from django.core.management.base import BaseCommand, CommandError
from django.core import files
from django.conf import settings
from products.models import Product
from products import amazon_utils
from PIL import Image, ImageChops

import math
import tempfile
import time

class Command(BaseCommand):
    products = Product.objects.all()
    amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID,
                       settings.AWS_SECRET_ACCESS_KEY,
                       settings.AWS_ASSOCIATE_TAG)

    for p in products:
        print "Fetching %s..." % p.asin
        az = amazon.lookup(ItemId=p.asin)
        lf, file_ext = amazon_utils.fetch_image(az.large_image_url)
        large_image = amazon_utils.fit_image(lf, (699, 875))
        thumb = amazon_utils.fit_image(lf, (285, 340), margin=100)
        p.image.save("%s-large.%s" % (p.product_id, file_ext), files.File(large_image))
        p.thumb.save("%s-small.%s" % (p.product_id, file_ext), files.File(thumb))
        time.sleep(1)
