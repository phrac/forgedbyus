from django import template
from products.models import Product

register = template.Library()

@register.simple_tag
def product_count():
    return Product.objects.all().count()
