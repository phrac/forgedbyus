from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'products.views.index'),
    url(r'^add/', 'products.views.add'),

]
