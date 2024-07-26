from django import forms
from .models import Support


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['full_name', 'email', 'support_type', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'support_type': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
