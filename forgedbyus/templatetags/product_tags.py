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

@register.simple_tag
def product_link(product_id, text):
    p = Product.objects.get(product_id=product_id)
    return "<a href=\"%s\">%s</a>" % (p.get_absolute_url(), text)

@register.filter
def render_db(value):
    from django.template import Template, Context
    return Template(value).render(Context())
