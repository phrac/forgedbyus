from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from products import urls as product_urls
from products import views as product_views
from products.models import Product, Collection
from . import views

product_dict = {
    'queryset': Product.objects.all().order_by('-created'),
    'date_field': 'created',
}
collection_dict = {
    'queryset': Collection.objects.all(),
    'date_field': 'updated',
}

sitemaps = {
    'products': GenericSitemap(product_dict, priority=0.6),
    'collections': GenericSitemap(collection_dict, priority=0.6)
}

urlpatterns = [
    url(r'^$', views.index),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/(?P<slug>[-\w]+)/$', product_views.details, name='product'),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/$', product_views.details, name='product'),

    url(r'^privacy/$', TemplateView.as_view(template_name="privacy.html"), name='privacy'),
    url(r'^disclaimer/$', TemplateView.as_view(template_name="disclaimer.html"), name='disclaimer'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),

    url(r'^search/', include('haystack.urls')),
    url(r'^collections/(?P<slug>[-\w]+)/$', product_views.collection, name='collections'),
    url(r'^products/', include(product_urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

from django.template.base import add_to_builtins
add_to_builtins('forgedbyus.templatetags.product_tags')
