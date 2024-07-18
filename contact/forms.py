# forms.py

from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'order_number', 'subject', 'content')
        widgets = {
            
        }
