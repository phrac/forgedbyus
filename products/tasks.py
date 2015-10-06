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
    print 'updating pricing'
    time_threshold = datetime.now() - timedelta(minutes=settings.UPDATE_PRICE_THRESHOLD)
    affiliate = Affiliate.objects.get(name='Amazon')
    products = Product.objects.filter(price_updated__lt=time_threshold, affiliate=affiliate)[:10]
    asins = [p.asin for p in products]
    asins_string = ','.join(asins)

    amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID,
                       settings.AWS_SECRET_ACCESS_KEY,
                       settings.AWS_ASSOCIATE_TAG)
    az = amazon.lookup(ItemId=asins_string)
    for p in az:
        if p.price_and_currency[0] is not None:
            product = Product.objects.get(asin=p.asin)
            product.current_price = int(math.ceil(p.price_and_currency[0]))
            product.price_updated = timezone.now()
            product.save()
