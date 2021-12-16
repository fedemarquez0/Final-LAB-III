from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bodega, Comentario, Estante, Origen, Variedad, Vino
from .forms import VinoForm, BodegaForm, OrigenForm, VariedadForm, EstanteForm, ComentarioForm, LoginForm, PasswordForm

from cart.forms import CartAddProductForm

from .api import get_valor, get_dolar

# Create your views here.

#Crea el agregar al carrito
def product_detail(request, id):
    vino = get_object_or_404(Vino, pk=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'cavovich/wine.html', {'vino': vino, 'cart_product_form': cart_product_form})

#Login
def loginUsuarios(request):
    return render(request, 'cavovich/login_list.html')

def loginLogin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Usuario o Contraseña no son validos')
    context = {'form': forms}
    return render(request, 'cavovich/login.html', context)

def loginSignin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = User.objects.create_user(username, 'pordefecto@mail.com', password)
            if user:
                return redirect('/')
    context = {'form': forms}
    return render(request, 'cavovich/signin.html', context)

def loginPassword(request):
    forms = PasswordForm()
    if request.method == 'POST':
        forms = PasswordForm(request.POST)
        if forms.is_valid():
            if request.user.is_authenticated:
                #password_old = forms.cleaned_data['password_old']
                password_new = forms.cleaned_data['password']
                username = request.user.username
                user = User.objects.get(username=username)
                user.set_password(password_new)
                user.save()
                #messages.success(request, 'Cambio de contraseña con exito')
                return redirect("/")
            else:
                messages.warning(request, 'No esta iniciado sesion')
    context = {'form': forms}
    return render(request, 'cavovich/password.html', context)

def loginLogout(request):
    logout(request)
    return redirect('/')

#Vino:
class Vinos(ListView): #Listar
    model = Vino
    template_name = 'cavovich/index.html'
    context_object_name = 'vinos_list'

class DetalleVino(DetailView): #vino por ID:
    model = Vino
    template_name = 'cavovich/wine.html'
    context_object_name = 'vino'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dolar'] = ("%.2f" % (get_valor() * float(context['vino'].precio)))
        return context


class VinoCreate(LoginRequiredMixin, CreateView): #Crear
    login_url = 'login'
    model = Vino
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"

class VinoUpdate(LoginRequiredMixin, UpdateView): #Modificar
    login_url = 'login'
    model = Vino
    template_name = 'cavovich/vino.html'
    form_class = VinoForm
    success_url = "/"

class VinoDelete(LoginRequiredMixin, DeleteView): #Eliminar
    model = Vino
    template_name = 'cavovich/eliminar.html'
    form_class = VinoForm
    success_url = "/"
    
#Bodega:
class BodegaList(LoginRequiredMixin, ListView): #Listar
    login_url = 'login'
    model = Bodega
    template_name = 'cavovich/bodega_list.html'
    context_object_name = 'bodegas_list'

class BodegaCreate(LoginRequiredMixin, CreateView): #Crear
    login_url = 'login'
    model = Bodega
    template_name = 'cavovich/bodega.html'
    form_class = BodegaForm
    success_url = "/bodega"

class BodegaUpdate(LoginRequiredMixin, UpdateView): #Modificar
    login_url = 'login'
    model = Bodega
    template_name = 'cavovich/bodega.html'
    form_class = BodegaForm
    success_url = "/bodega"

class BodegaDelete(LoginRequiredMixin, DeleteView): #Eliminar
    login_url = 'login'
    model = Bodega
    template_name = 'cavovich/eliminar.html'
    form_class = BodegaForm
    success_url = "/bodega"

#Origen:
class OrigenList(LoginRequiredMixin, ListView): #Listar
    login_url = 'login'
    model = Origen
    template_name = 'cavovich/origen_list.html'
    context_object_name = 'origen_list'

class OrigenCreate(LoginRequiredMixin, CreateView): #Crear
    login_url = 'login'
    model = Origen
    template_name = 'cavovich/origen.html'
    form_class = OrigenForm
    success_url = "/origen"

class OrigenUpdate(LoginRequiredMixin, UpdateView): #Modificar
    login_url = 'login'
    model = Origen
    template_name = 'cavovich/origen.html'
    form_class = OrigenForm
    success_url = "/origen"

class OrigenDelete(LoginRequiredMixin, DeleteView): #Eliminar
    login_url = 'login'
    model = Origen
    template_name = 'cavovich/eliminar.html'
    form_class = OrigenForm
    success_url = "/origen"

#Variedad:
class VariedadList(LoginRequiredMixin, ListView): #Listar
    login_url = 'login'
    model = Variedad
    template_name = 'cavovich/variedad_list.html'
    context_object_name = 'variedad_list'

class VariedadCreate(LoginRequiredMixin, CreateView): #Crear
    login_url = 'login'
    model = Variedad
    template_name = 'cavovich/variedad.html'
    form_class = VariedadForm
    success_url = "/variedad"

class VariedadUpdate(LoginRequiredMixin, UpdateView): #Modificar
    login_url = 'login'
    model = Variedad
    template_name = 'cavovich/variedad.html'
    form_class = VariedadForm
    success_url = "/variedad"

class VariedadDelete(LoginRequiredMixin, DeleteView): #Eliminar
    login_url = 'login'
    model = Variedad
    template_name = 'cavovich/eliminar.html'
    form_class = VariedadForm
    success_url = "/variedad"

#Estante:
class EstanteList(LoginRequiredMixin, ListView): #Listar
    login_url = 'login'
    model = Estante
    template_name = 'cavovich/estantes_list.html'
    context_object_name = 'estantes_list'

class EstanteCreate(LoginRequiredMixin, CreateView): #Crear
    login_url = 'login'
    model = Estante
    template_name = 'cavovich/estante.html'
    form_class = EstanteForm
    success_url = "/estante"

class EstanteUpdate(LoginRequiredMixin, UpdateView): #Modificar
    login_url = 'login'
    model = Estante
    template_name = 'cavovich/estante.html'
    form_class = EstanteForm
    success_url = "/estante"

class EstanteDelete(LoginRequiredMixin, DeleteView): #Eliminar
    login_url = 'login'
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
