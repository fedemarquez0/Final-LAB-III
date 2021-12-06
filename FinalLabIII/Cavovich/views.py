from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView, CreateView, DetailView
from .forms import UploadImageForm

from .models import Vino
from .forms import VinoForm, BodegaForm, OrigenForm, VariedadForm, EstanteForm

# Create your views here.

#muestra todos los vinos:
class Vinos(ListView): #sirve para traer toda la info de la base de datos
    model = Vino
    template_name = 'cavovich/all_wines.html'
    context_object_name = 'vinos_list'

#muestra un solo vino por ID:
class DetalleVino(DetailView):
    model = Vino
    template_name = 'cavovich/wine.html'
    context_object_name = 'vino'

#clases para hacer los formularios
class VinoSave(CreateView):
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Vino.objects.all()
        return context

class BodegaSave(CreateView):
    template_name = 'cavovich/bodega.html'
    form_class = BodegaForm
    success_url = "/"

class OrigenSave(CreateView):
    template_name = 'cavovich/origen.html'
    form_class = OrigenForm
    success_url = "/"

class VariedadSave(CreateView):
    template_name = 'cavovich/variedad.html'
    form_class = VariedadForm
    success_url = "/"

class EstanteSave(CreateView):
    template_name = 'cavovich/estante.html'
    form_class = EstanteForm
    success_url = "/"
<<<<<<< HEAD
=======

    def form_valid(self, form):
        form.save()
        return super(EstanteForm, self).form_valid(form)

#muestra todos los vinos
class allVinos(ListView): #sirve para traer toda la info de la base de datos
    model = Vino
    template_name = 'cavovich/index.html'
    context_object_name = 'vinos_list'
>>>>>>> 8ac090339fb56acf15c24fdc5fed02360a238a40
