from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from haystack.query import SearchQuerySet

from products.forms import NewAmazonProductForm, ProductForm
from products.models import Product
from products import amazon_utils


def index(request):
    pass

def category_index(request):
    return render(request, 'category_index.html')

def details(request, product_id):
    product = Product.objects.get(product_id=product_id)
    mlt = SearchQuerySet().more_like_this(product)
    return render(request, 'details.html', {'product':product, 'related':mlt})

@staff_member_required
def add_asin(request):
    if request.method == 'POST':
        form = NewAmazonProductForm(request.POST)
        if form.is_valid():
            product = amazon_utils.get_asin(form.cleaned_data['asin'].strip().upper())
            return redirect('products.views.add_product', product_id=product.product_id)
    else:
        form = NewAmazonProductForm()

    return render(request, 'add_asin.html', {'form': form})

@staff_member_required
def add_product(request, product_id=None):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        productform = ProductForm(request.POST, instance=product)
        if productform.is_valid():
            product = productform.save()
            return HttpResponseRedirect(product.get_absolute_url())
    else:
        productform = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': productform})
