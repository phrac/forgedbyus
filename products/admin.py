from django.contrib import admin
from products.models import Product, ProductImage, Collection, Category

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Collection)
admin.site.register(Category)
