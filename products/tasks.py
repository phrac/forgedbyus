from amazon.api import AmazonAPI
from celery import task
from products.models import Product
from affiliates.models import Affiliate

from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone

import math

@task
def update_price():
    time_threshold = timezone.now() - timedelta(minutes=settings.UPDATE_PRICE_THRESHOLD)
    affiliate = Affiliate.objects.get(name='Amazon')
    products = Product.objects.filter(price_updated__lt=time_threshold, affiliate=affiliate)[:10]
    if len(products) > 0:
        asins = [p.asin for p in products]
        asins_string = ','.join(asins)

        amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID,
                           settings.AWS_SECRET_ACCESS_KEY,
                           settings.AWS_ASSOCIATE_TAG)
        az = amazon.lookup(ItemId=asins_string)
        if type(az) is list:
            for p in az:
                process_item(p)
        else:
            process_item(az)

def process_item(item):
    if item.price_and_currency[0] is not None:
        product = Product.objects.get(asin=item.asin)
        product.current_price = int(math.ceil(item.price_and_currency[0]))
        product.price_updated = timezone.now()
        product.save()
