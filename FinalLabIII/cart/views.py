from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.conf import settings
 
#from shop.models import Product
from Cavovich.models import Vino
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Vino, pk=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Vino, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def decrementarStock(request):
    cart = Cart(request)
    for item in cart:
        print(item)
        item['product'].stock(item['quantity'])
    cart.clear()
    cart = {}
    return redirect('/')