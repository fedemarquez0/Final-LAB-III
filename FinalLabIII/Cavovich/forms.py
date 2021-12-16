from django import forms
from django.forms import fields
from .models import Comentario, Vino, Bodega, Origen, Variedad, Estante

class VinoForm(forms.ModelForm):
    # nombre = forms.CharField(widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'type': 'text'
    #     }))
    # bodega = forms.CharField(widget=forms.Select(choices=Bodega.objects.all().values_list(),attrs={
    #     'class': 'form-control'
    # }))
    # variedad = forms.CharField(widget=forms.Select(choices=Variedad.objects.all().values_list() ,attrs={
    #     'class': 'form-control'
    # }))
    # cosecha = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'date'
    # }))
    # origen = forms.CharField(widget=forms.Select(choices=Origen.objects.all().values_list() ,attrs={
    #     'class': 'form-control'
    # }))
    # cantidad = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'number'
    # }))
    # codigo = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'number'
    # }))
    # precio = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'number'
    # }))
    # estante = forms.CharField(widget=forms.Select(choices=Estante.objects.all().values_list() ,attrs={
    #     'class': 'form-control'
    # }))

    class Meta:
        
        model = Vino
        fields = '__all__'
        
        

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

class OrigenForm(forms.ModelForm):
    class Meta:
        model = Origen
        fields = '__all__'

class VariedadForm(forms.ModelForm):
    class Meta:
        model = Variedad
        fields = '__all__'

class EstanteForm(forms.ModelForm):
    class Meta:
        model = Estante
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Usuario',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
        'type': 'password'
    }))

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
        'type': 'password'
    }))