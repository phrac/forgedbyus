from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^departments/$', views.category_index),
    url(r'^departments/(?P<slug>[-\w]+)/$', views.category, name='category'),
    url(r'^add_asin/', views.add_asin),
    url(r'^add_product/(?P<product_id>[A-Z0-9]{10})/$', views.add_product),
    url(r'^add_collection/$', views.add_collection),

]
