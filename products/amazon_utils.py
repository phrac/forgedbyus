from amazon.api import AmazonAPI
from django.conf import settings
from products.models import Product
from words.models import Word
from random import choice, randint


def get_or_create_product(asin):
    """
    Checks the database for an existing ASIN. If not found, try to fetch it
    using the Amazon Product API.

    :return:
        An instance of `products.models.Product`
    """
    try:
        product = Product.objects.get(asin=asin)
    except:
        amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID,
                           settings.AWS_SECRET_ACCESS_KEY,
                           settings.AWS_ASSOCIATE_TAG)
        az = amazon.lookup(ItemId=asin)
        product = Product(asin=asin, upc=az.upc, ean=az.ean,
                          description=az.title, image_url=az.large_image_url,
                          amazon_url=az.offer_url)

        product.save()

    return product
