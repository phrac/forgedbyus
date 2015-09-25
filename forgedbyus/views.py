from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from products.models import Product

def index(request):
    products = Product.objects.all().order_by('-created')[:8]
    return render(request,
                    'index.html',
                    {
                        'products':products,
                    })
