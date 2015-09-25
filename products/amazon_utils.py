from amazon.api import AmazonAPI
from django.conf import settings
import requests
import tempfile

from django.core import files
from products.models import Product, ProductImage
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
        image = ProductImage(product_id=product.id)
        lf, file_ext = fetch_image(az.large_image_url)
        image_num = ProductImage.objects.filter(product_id=product.id).count() + 1
        image.image.save("%s-%s.%s" % (product.product_id, image_num, file_ext), files.File(lf))
        image.save()


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
