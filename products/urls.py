from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'products.views.index'),
    url(r'^fbu/(?P<product_id>.+)/$', 'products.views.details'),
    url(r'^add_asin/', 'products.views.add_asin'),
    url(r'^add_product/(?P<product_id>.+)$', 'products.views.add_product'),

]
