from django import forms
from django.forms import fields
from .models import Vino, Bodega, Origen, Variedad, Estante

class VinoForm(forms.ModelForm):
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