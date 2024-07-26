from django import forms
from django.forms import ModelForm

from myapp.models import Order, Review, Contact, Ecoproducts, Participant

class EcoproductsSearchForm(forms.Form):
    name = forms.CharField(label='Product Name', max_length=255, required=False)
    category = forms.ChoiceField(label='Category', choices=Ecoproducts.CATEGORY_CHOICES, required=False)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2, required=False)
