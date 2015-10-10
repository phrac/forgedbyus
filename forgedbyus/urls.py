from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from products import urls as product_urls
from products import views as product_views
from products.models import Product
from . import views

info_dict = {
    'queryset': Product.objects.all(),
    'date_field': 'created',
}

urlpatterns = [
    url(r'^$', views.index),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/(?P<slug>[-\w]+)/$', product_views.details, name='product'),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/$', product_views.details, name='product'),

    url(r'^privacy/$', TemplateView.as_view(template_name="privacy.html"), name='privacy'),
    url(r'^disclaimer/$', TemplateView.as_view(template_name="disclaimer.html"), name='disclaimer'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),

    url(r'^search/', include('haystack.urls')),
    url(r'^products/', include(product_urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'products': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
