from django.db import models

def id_generator():
    return 'fbu'.join(random.choice(string.ascii_uppercase + string.digits) for x in range(7))

class Product(models.Model):
    product_id = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=64)
    asin = models.CharField(max_length=10, null=True, blank=True)
    brand = models.CharField(max_length=128, null=True)
    manufacturer = models.CharField(max_length=128, null=True)
    state_of_origin = models.CharField(max_length=2, null=True, blank=True)
    usa_verified = models.BooleanField(default=False)
    short_description = models.TextField()
    description = models.TextField()
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, null=True)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = id_generator()
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField()
    thumb = models.ImageField()
