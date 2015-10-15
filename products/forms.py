from django import forms
from django.forms import ModelForm

from products.models import Product, Collection

class NewAmazonProductForm(forms.Form):
    asin = forms.CharField(label='ASIN')

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('product_id', 'created', 'detail_views', 'sales_rank', 'user')

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        exclude = ('created', 'updated')
