from django.conf.urls import include, url
from django.contrib import admin

from products import urls as product_urls
from products import views as product_views
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/(?P<slug>[-\w]+)/$', product_views.details, name='product'),
    url(r'^fbu/(?P<product_id>[A-Z0-9]{10})/$', product_views.details, name='product'),
    url(r'^search/', include('haystack.urls')),
    url(r'^products/', include(product_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
