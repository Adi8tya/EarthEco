from django import forms
from . models import Blogs

class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','author', 'content','header_image')


        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }