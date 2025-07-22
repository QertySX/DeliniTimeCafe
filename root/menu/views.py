from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def menu(request):
    products = Product.objects.all()
    category = Category.objects.all()

    selected_category_id = request.GET.get('category')

    if selected_category_id:
        products = products.filter(category__id=selected_category_id)


    return render(request, 'menu/menu.html', context={
        'title': 'Меню',
        'page': 'menu',
        'app': 'menu',
        'products': products,
        'category': category,
        'selected_category_id': selected_category_id,
    })
