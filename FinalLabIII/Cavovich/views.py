from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Bodega, Comentario, Estante, Origen, Variedad, Vino
from .forms import VinoForm, BodegaForm, OrigenForm, VariedadForm, EstanteForm, ComentarioForm, LoginForm

from cart.forms import CartAddProductForm

# Create your views here.

#crea el agregar al carrito
def product_detail(request, id):
    vino = get_object_or_404(Vino, pk=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'cavovich/wine.html', {'vino': vino, 'cart_product_form': cart_product_form})

#login
def login_pagina(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('')
    context = {'form': forms}
    return render(request, 'cavovich/signin.html', context)

def logout_pagina(request):
    logout(request)
    return redirect('cavovich/signin.html')

#Vino:
class Vinos(ListView): #Listar
    model = Vino
    template_name = 'cavovich/index.html'
    context_object_name = 'vinos_list'

class DetalleVino(DetailView): #vino por ID:
    model = Vino
    template_name = 'cavovich/wine.html'
    context_object_name = 'vino'

class VinoCreate(CreateView): #Crear
    model = Vino
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"

class VinoUpdate(UpdateView): #Modificar
    model = Vino
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"

class VinoDelete(DeleteView): #Eliminar
    model = Vino
    template_name = 'cavovich/eliminar.html'
    form_class = VinoForm
    success_url = "/"
    
#Bodega:
class BodegaList(ListView): #Listar
    model = Bodega
    template_name = 'cavovich/bodega_list.html'
    context_object_name = 'bodegas_list'

class BodegaCreate(CreateView): #Crear
    model = Bodega
    template_name = 'cavovich/bodega.html'
    form_class = BodegaForm
    success_url = "/bodega"

class BodegaUpdate(UpdateView): #Modificar
    model = Bodega
    template_name = 'cavovich/bodega.html'
    form_class = BodegaForm
    success_url = "/bodega"

class BodegaDelete(DeleteView): #Eliminar
    model = Bodega
    template_name = 'cavovich/eliminar.html'
    form_class = BodegaForm
    success_url = "/bodega"

#Origen:
class OrigenList(ListView): #Listar
    model = Origen
    template_name = 'cavovich/origen_list.html'
    context_object_name = 'origen_list'

class OrigenCreate(CreateView): #Crear
    model = Origen
    template_name = 'cavovich/origen.html'
    form_class = OrigenForm
    success_url = "/origen"

class OrigenUpdate(UpdateView): #Modificar
    model = Origen
    template_name = 'cavovich/origen.html'
    form_class = OrigenForm
    success_url = "/origen"

class OrigenDelete(DeleteView): #Eliminar
    model = Origen
    template_name = 'cavovich/eliminar.html'
    form_class = OrigenForm
    success_url = "/origen"

#Variedad:
class VariedadList(ListView): #Listar
    model = Variedad
    template_name = 'cavovich/variedad_list.html'
    context_object_name = 'variedad_list'

class VariedadCreate(CreateView): #Crear
    model = Variedad
    template_name = 'cavovich/variedad.html'
    form_class = VariedadForm
    success_url = "/variedad"

class VariedadUpdate(UpdateView): #Modificar
    model = Variedad
    template_name = 'cavovich/variedad.html'
    form_class = VariedadForm
    success_url = "/variedad"

class VariedadDelete(DeleteView): #Eliminar
    model = Variedad
    template_name = 'cavovich/eliminar.html'
    form_class = VariedadForm
    success_url = "/variedad"

#Estante:
class EstanteList(ListView): #Listar
    model = Estante
    template_name = 'cavovich/estantes_list.html'
    context_object_name = 'estantes_list'

class EstanteCreate(CreateView): #Crear
    model = Estante
    template_name = 'cavovich/estante.html'
    form_class = EstanteForm
    success_url = "/estante"

class EstanteUpdate(UpdateView): #Modificar
    model = Estante
    template_name = 'cavovich/estante.html'
    form_class = EstanteForm
    success_url = "/estante"

class EstanteDelete(DeleteView): #Eliminar
    model = Estante
    template_name = 'cavovich/eliminar.html'
    form_class = EstanteForm
    success_url = "/estante"

#Comentario:
# class ComentarioCreate(CreateView): #Crear
#     model = Comentario
#     template_name = 'cavovich/comentario.html'
#     form_class = ComentarioForm
#     success_url = "/"

# class ComentarioUpdate(UpdateView): #Modificar
#     model = Comentario
#     template_name = 'cavovich/comentario.html'
#     form_class = ComentarioForm
#     success_url = "/"

# class ComentarioDelete(DeleteView): #Eliminar
#     model = Comentario
#     template_name = 'cavovich/eliminar.html'
#     form_class = ComentarioForm
#     success_url = "/"
