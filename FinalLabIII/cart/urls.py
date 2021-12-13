from django.conf.urls import url, include
from django.urls import path
from . import views
 
urlpatterns = [
    # url(r'^$', views.cart_detail, name='cart_detail'),
    # url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    # url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'), 

    path('remove/<int:product_id>/', views.cart_add, name='cart_remove'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('', views.cart_detail, name='cart_detail'),
    ]