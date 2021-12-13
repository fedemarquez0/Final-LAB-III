from  django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'number',
        }))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    