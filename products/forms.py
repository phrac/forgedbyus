from django import forms
from django.forms import ModelForm

class NewAmazonProductForm(forms.Form):
    asin = forms.CharField(label='ASIN')
