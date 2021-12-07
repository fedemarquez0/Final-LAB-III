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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Vinos.as_view()),
    path('vino/', VinoCreate.as_view()),
    path('bodega/', BodegaCreate.as_view()),
    path('origen/', OrigenCreate.as_view()),
    path('variedad/', VariedadCreate.as_view()),
    path('estante/', EstanteCreate.as_view()),
    path('vino/<int:pk>', DetalleVino.as_view()),
    path('update/<int:pk>/', VinoUpdate.as_view()),
    path('delete/<int:pk>/', VinoDelete.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
