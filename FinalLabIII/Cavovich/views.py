from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Bodega, Comentario, Estante, Origen, Variedad, Vino
from .forms import VinoForm, BodegaForm, OrigenForm, VariedadForm, EstanteForm, ComentarioForm, LoginForm

from cart.forms import CartAddProductForm

# Create your views here.

def product_detail(request, id):
    vino = get_object_or_404(Vino, pk=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'cavovich/wine.html', {'vino': vino, 'cart_product_form': cart_product_form})

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

class ComentarioCreate(CreateView):
    model = Comentario
    template_name = 'cavovich/comentario.html'
    form_class = ComentarioForm
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


#funcion para incrementar stock
def incrementarStock(request: HttpRequest, id_vino: int, cantidad: int):
    vino = Vino.objects.get(id = id_vino)
    vino.cantidad += cantidad
    vino.save()
    # messages.info(request, 'Your password has been changed successfully!')
    return redirect("inicio")