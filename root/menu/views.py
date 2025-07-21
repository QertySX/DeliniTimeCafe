from django.shortcuts import render
from .models import Product, Category

def menu(request):
    product = Product.objects.all()
    return render(request, 'menu/menu.html', context={
        'title': 'Меню',
        'page': 'menu',
        'app': 'menu',
        'product': product
    })
