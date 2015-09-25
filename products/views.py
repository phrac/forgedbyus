from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

from products.forms import NewAmazonProductForm
from products import amazon_utils


def index(request):
    pass

    
def add(request):
    if request.method == 'POST':
        form = NewAmazonProductForm(request.POST)
        if form.is_valid():
            product = amazon_utils.get_asin(form.cleaned_data['asin'].strip().upper())
            return HTTPResponseRedirect('/products/add/')
    else:
        form = NewAmazonProductForm()

    return render(request, 'add.html', {'form': form})
