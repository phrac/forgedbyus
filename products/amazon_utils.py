from amazon.api import AmazonAPI
from django.conf import settings
import requests
import tempfile

from django.core import files
from products.models import Product
from affiliates.models import Affiliate
from brands.models import Brand
from PIL import Image, ImageChops

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
        parsed_features = [s for s in az.features if len(s) < 127]
        product = Product(
                          affiliate=afid,
                          asin=asin,
                          short_description=az.title,
                          title=title,
                          brand=brand,
                          manufacturer=az.manufacturer,
                          current_price=price,
                          msrp=msrp,
                          features=parsed_features,
                          user=user,
                          sales_rank=az.sales_rank,
                          )

        product.save()
        lf, file_ext = fetch_image(az.large_image_url)
        large_image = fit_image(lf, (699, 875))
        thumb = fit_image(lf, (285, 340), margin=100)
        product.image.save("%s-large.%s" % (product.product_id, file_ext), files.File(large_image))
        product.thumb.save("%s-small.%s" % (product.product_id, file_ext), files.File(thumb))


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

def fit_image(img, new_size, margin=0):
    import StringIO
    fit_io = StringIO.StringIO()

    image = Image.open(img)

    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    bbox = diff.getbbox()
    image.crop(bbox)


    image.thumbnail(new_size, Image.ANTIALIAS)
    old_size = image.size
    if old_size[1] == new_size[1]:
        tmp_size = (old_size[0], old_size[1] - margin)
        image.thumbnail(tmp_size, Image.ANTIALIAS)
    # scale image and paste to correct size
    old_size = image.size
    scaled = Image.new("RGB", new_size, "white")
    scaled.paste(image, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))

    scaled.save(fit_io, "JPEG")
    return fit_io
