"""FinalLabIII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from config import settings
from Cavovich.views import *


from django.conf import settings
from django.conf.urls import url, include
from cart import *
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),

    path('cart/',include(('cart.urls', 'cart'), namespace='cart')),

    path('login/', login_pagina, name='login'),

    path('', Vinos.as_view(), name='inicio'),
    path('vino/', VinoCreate.as_view(), name='verVinos'),
    path('vino/<int:pk>', DetalleVino.as_view()),
    path('vino/update/<int:pk>/', VinoUpdate.as_view()),
    path('vino/delete/<int:pk>/', VinoDelete.as_view()),

    path('bodega/', BodegaList.as_view(), name='verBodega'),
    path('bodega/create/', BodegaCreate.as_view()),
    path('bodega/update/<int:pk>/', BodegaUpdate.as_view()),
    path('bodega/delete/<int:pk>/', BodegaDelete.as_view()),

    path('origen/', OrigenList.as_view(), name='verOrigen'),
    path('origen/create/', OrigenCreate.as_view()),
    path('origen/update/<int:pk>/', OrigenUpdate.as_view()),
    path('origen/delete/<int:pk>/', OrigenDelete.as_view()),

    path('variedad/', VariedadList.as_view(), name='verVariedad'),
    path('variedad/create/', VariedadCreate.as_view()),
    path('variedad/update/<int:pk>/', VariedadUpdate.as_view()),
    path('variedad/delete/<int:pk>/', VariedadDelete.as_view()),

    path('estante/', EstanteList.as_view(), name='verEstantes'),
    path('estante/create/', EstanteCreate.as_view()),
    path('estante/update/<int:pk>/', EstanteUpdate.as_view()),
    path('estante/delete/<int:pk>/', EstanteDelete.as_view()),

    # path('comentario/create/', ComentarioCreate.as_view()),
    # path('comentario/update/<int:pk>/', ComentarioUpdate.as_view()),
    # path('comentario/delete/<int:pk>/', ComentarioDelete.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
