from django.conf.urls import url, include
from django.urls import path
from . import views
 
urlpatterns = [
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('', views.cart_detail, name='cart_detail'),
]
