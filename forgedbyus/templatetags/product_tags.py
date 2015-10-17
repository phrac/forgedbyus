from django import template
from products.models import Product, Collection

register = template.Library()

@register.simple_tag
def product_count():
    return Product.objects.all().count()

@register.inclusion_tag('collection_banners.html')
def collection_banners():
    collections = Collection.objects.filter(featured=True).order_by('-created')[:4]
    return {'collections': collections}
