from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        labels = {'name': 'название продукта', 'description': 'Описание продукта', 'price': 'Стоимость за 100гр.'}