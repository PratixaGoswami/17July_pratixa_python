from django import forms
from .models import*

class ProductForm(forms.ModelForm):
    class Meta:
        model = product_mst
        fields = ['product_name']

    price = forms.DecimalField(max_digits=10, decimal_places=2)
    image = forms.ImageField()
    model = forms.CharField(max_length=100)
    ram = forms.CharField(max_length=50)