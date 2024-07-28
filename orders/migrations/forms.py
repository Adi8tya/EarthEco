from django import forms
class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        quantity = forms.IntegerField(min_value=1)
        fields = ['quantity']


class CheckoutForm(forms.Form):
    address = forms.CharField(label='Shipping Address')
class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['profile_image']