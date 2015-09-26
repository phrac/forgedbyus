from django import forms
from django.forms import ModelForm

from products.models import Product

class NewAmazonProductForm(forms.Form):
    asin = forms.CharField(label='ASIN')

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('product_id', 'created',)
