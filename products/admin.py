from django.contrib import admin
from products.models import Product, ProductImage, Collection

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Collection)
