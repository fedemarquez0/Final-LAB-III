from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import EmptyQuerySet

from .models import Bodega, Comentario, Estante, Origen, Variedad, Vino
from .forms import VinoForm, BodegaForm, OrigenForm, VariedadForm, EstanteForm, ComentarioForm, LoginForm, PasswordForm

from cart.forms import CartAddProductForm

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
    if not request.user.is_authenticated:
        return redirect('login')
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
def vinos(request): #Listar (opcion para buscar)
    if request.method == 'GET':
        search = request.GET.get('search')
        if search == None:
            all_vinos = Vino.objects.all()
            return render(request, 'cavovich/index.html', {'vinos_list':all_vinos, 'buscador':''})
        else:
            vinos_list_nombre = Vino.objects.filter(nombre__contains = search)
            vinos_list_bodega = Vino.objects.filter(bodega__bodega__contains = search)
            vinos_list_variedad = Vino.objects.filter(variedad__variedad__contains = search)
            vinos_list_cosecha = Vino.objects.filter(cosecha__contains = search)
            vinos_list_origen = Vino.objects.filter(origen__origen__contains = search)
            vinos_list_codigo = Vino.objects.filter(codigo__contains = search)
            vinos_list_estante = Vino.objects.filter(estante__estante__contains = search)
            vinos_list = vinos_list_nombre.union(vinos_list_bodega, vinos_list_variedad, vinos_list_cosecha, vinos_list_origen, vinos_list_codigo, vinos_list_estante)
            return render(request, 'cavovich/index.html', {'vinos_list':vinos_list, 'buscador': search})

class DetalleVino(DetailView): #vino por ID:
    model = Vino
    template_name = 'cavovich/wine.html'
    context_object_name = 'vino'

def agregarVino(request):
    codigo_barras = request.GET.get('codigo_barras')
    if codigo_barras != None:
        vino = Vino.objects.filter(codigo = codigo_barras) 
        if vino.exists():
            return render(request, 'cavovich/incrementar.html', {'vino':vino.first()})
        else:
            return redirect('/vino/') #Falta autocompletar el valor del codigo de barras.

    return render(request, 'cavovich/agregar.html')

def incrementarStockVino(request):
    cantidad = int(request.GET.get('cantidad'))
    vinoId = request.GET.get('vinoId')
    if cantidad != None and vinoId != None:
        vino = Vino.objects.filter(id = vinoId).first()
        vino.incrementarStock(cantidad)
        print(f"vino: {vino}")
    return redirect('/')

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
    login_url = 'login'
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
