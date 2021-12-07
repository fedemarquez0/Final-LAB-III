from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView, CreateView, DetailView, UpdateView, DeleteView

from .models import Bodega, Estante, Origen, Variedad, Vino
from .forms import VinoForm, BodegaForm, OrigenForm, VariedadForm, EstanteForm

# Create your views here.

#muestra todos los vinos:
class Vinos(ListView): #sirve para traer toda la info de la base de datos
    model = Vino
    template_name = 'cavovich/index.html'
    context_object_name = 'vinos_list'

#muestra un solo vino por ID:
class DetalleVino(DetailView):
    model = Vino
    template_name = 'cavovich/wine.html'
    context_object_name = 'vino'

#clases para crear
class VinoCreate(CreateView):
    model = Vino
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"

class BodegaCreate(CreateView):
    model = Bodega
    template_name = 'cavovich/bodega.html'
    form_class = BodegaForm
    success_url = "/"

class OrigenCreate(CreateView):
    model = Origen
    template_name = 'cavovich/origen.html'
    form_class = OrigenForm
    success_url = "/"

class VariedadCreate(CreateView):
    model = Variedad
    template_name = 'cavovich/variedad.html'
    form_class = VariedadForm
    success_url = "/"

class EstanteCreate(CreateView):
    model = Estante
    template_name = 'cavovich/estante.html'
    form_class = EstanteForm
    success_url = "/"

#clases para modificar
class VinoUpdate(UpdateView):
    model = Vino
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"

#clases para eliminar
class VinoDelete(DeleteView):
    model = Vino
    template_name = 'cavovich/eliminar.html'
    form_class = VinoForm
    success_url = "/"

