from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from products.models import Product

def index(request):
    return render(request, 'index.html')
