from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404

from products.forms import NewAmazonProductForm, ProductForm
from products.models import Product, Category
from products.tasks import update_detail_views
from products import amazon_utils
from slugify import slugify


def index(request):
    pass

def category_index(request):
    categories = Category.objects.all()
    return render(request, 'category_index.html', {'categories':categories})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category':category, 'products':products})

def details(request, product_id, slug=None):
    product = get_object_or_404(Product, product_id=product_id)
    update_detail_views.delay(product.id)

    title = slugify(product.title, max_length=50, separator=' ', capitalize=True)
    if slug is None and product.slug is not None:
        return HttpResponsePermanentRedirect(reverse('products.views.details', args=[product.product_id, product.slug]))
    if slug != product.slug:
        return HttpResponsePermanentRedirect(reverse('products.views.details', args=[product.product_id, product.slug]))
    if request.is_ajax():
        template = 'product_modal_content.html'
    else:
        template = 'details.html'
    return render(request, template, {'product':product, 'title':title})

def collection(request, slug):
    pass

@staff_member_required
def add_asin(request):
    if request.method == 'POST':
        form = NewAmazonProductForm(request.POST)
        if form.is_valid():
            product = amazon_utils.get_asin(form.cleaned_data['asin'].strip().upper(), request.user)
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
