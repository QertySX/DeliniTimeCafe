from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html', context={
        'title': 'Головна',
        'page': 'index',
        'app': 'home',
    })


def about(request):
    '''ДОБАВИТЬ КОШИК'''
    return render(request, 'home/about.html', context={
        'title': 'Про нас ',
        'page': 'about',
        'app': 'home',
    })