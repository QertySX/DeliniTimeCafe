from django.urls import path
from .views import ajax_cart, reserv, ajax_cart_indicate

urlpatterns = [
    path('ajax_cart', ajax_cart),
    path('index', reserv, name='reserv'),
    path('ajax_cart_indicate', ajax_cart_indicate),
]