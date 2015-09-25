from amazon.api import AmazonAPI
from django.conf import settings
from products.models import Product
from affiliates.models import Affiliate

import math


def get_asin(asin):
    """
    Checks the database for an existing ASIN. If not found, try to fetch it
    using the Amazon Product API.

    :return:
        An instance of `products.models.Product`
    """
    afid = Affiliate.objects.get(name='Amazon')
    try:
        product = Product.objects.get(asin=asin)
    except:
        amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID,
                           settings.AWS_SECRET_ACCESS_KEY,
                           settings.AWS_ASSOCIATE_TAG)
        az = amazon.lookup(ItemId=asin)
        price = int(math.ceil(az.price_and_currency[0]))
        title = az.title.split(',', 1)[0]
        product = Product(
                          affiliate_id=afid,
                          asin=asin,
                          short_description=az.title,
                          title=title,
                          brand=az.brand,
                          manufacturer=az.manufacturer,
                          current_price=price,
                          )

        product.save()

    return product
