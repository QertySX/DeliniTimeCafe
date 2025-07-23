from django.urls import path
from .views import menu, delivery

urlpatterns = [
    path('', menu, name='menu'),
    path('delivery', delivery ,name='delivery')
]