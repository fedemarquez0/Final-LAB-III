from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView

from .models import Vino
from .forms import VinoForm, BodegaForm, OrigenForm, VariedadForm, EstanteForm

# Create your views here.

#muestra todos los vinos
class Vinos(ListView): #sirve para traer toda la info de la base de datos
    model = Vino
    template_name = 'cavovich/all_wines.html'
    context_object_name = 'vinos_list'

#clases para hacer los formularios
class VinoSave(FormView):
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(VinoForm, self).form_valid(form)

class BodegaSave(FormView):
    template_name = 'cavovich/bodega.html'
    form_class = BodegaForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(BodegaForm, self).form_valid(form)

class OrigenSave(FormView):
    template_name = 'cavovich/origen.html'
    form_class = OrigenForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(OrigenForm, self).form_valid(form)

class VariedadSave(FormView):
    template_name = 'cavovich/variedad.html'
    form_class = VariedadForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(VariedadForm, self).form_valid(form)

class EstanteSave(FormView):
    template_name = 'cavovich/estante.html'
    form_class = EstanteForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(EstanteForm, self).form_valid(form)

#muestra todos los vinos
class allVinos(ListView): #sirve para traer toda la info de la base de datos
    model = Vino
    template_name = 'cavovich/index.html'
    context_object_name = 'vinos_list'
