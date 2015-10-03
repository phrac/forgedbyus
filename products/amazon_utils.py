from amazon.api import AmazonAPI
from django.conf import settings
import requests
import tempfile

from django.core import files
from products.models import Product
from affiliates.models import Affiliate
from brands.models import Brand

import math


def get_asin(asin, user=None):
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
        if az.list_price[0] is not None:
            msrp = int(math.ceil(az.list_price[0]))
        else:
            msrp = None
        title = az.title.split(',', 1)[0]
        title = title.split('(', 1)[0]
        brand, _created = Brand.objects.get_or_create(name=az.brand)
        product = Product(
                          affiliate=afid,
                          asin=asin,
                          short_description=az.title,
                          title=title,
                          brand=brand,
                          manufacturer=az.manufacturer,
                          current_price=price,
                          msrp=msrp,
                          features=az.features,
                          user=user,
                          sales_rank=az.sales_rank,
                          )

        product.save()
        lf, file_ext = fetch_image(az.large_image_url)
        product.image.save("%s.%s" % (product.product_id, file_ext), files.File(lf))
        #product.save()


    return product

def fetch_image(url):
    # Steam the image from the url
    request = requests.get(url, stream=True)

    # Get the filename from the url, used for saving later
    file_name = url.split('/')[-1]
    file_ext = file_name.split('.')[-1]

    # Create a temporary file
    lf = tempfile.NamedTemporaryFile()

    # Read the streamed image in sections
    for block in request.iter_content(1024 * 8):

        # If no more file then stop
        if not block:
            break

        # Write image block to temporary file
        lf.write(block)
    return lf, file_ext
    # Create the model you want to save the image to
    #image = Image()

    # Save the temporary image to the model#
    # This saves the model so be sure that is it valid
    #image.image.save(file_name, files.File(lf))
