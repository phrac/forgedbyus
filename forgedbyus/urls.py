from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from products import urls as product_urls
from products import views as product_views
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/(?P<slug>[-\w]+)/$', product_views.details, name='product'),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/$', product_views.details, name='product'),

    url(r'^privacy/', TemplateView.as_view(template_name="privacy.html"), name='privacy'),
    url(r'^disclaimer/', TemplateView.as_view(template_name="disclaimer.html"), name='disclaimer'),


    url(r'^search/', include('haystack.urls')),
    url(r'^products/', include(product_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
