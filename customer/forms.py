from django import forms
from .models import CartItem,Order


class Cartform(forms.ModelForm):
    class Meta:
        model=CartItem
        fields=["quantity"]
        

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"