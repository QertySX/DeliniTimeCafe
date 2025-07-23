from django.shortcuts import render, redirect
from .models import BookTable

# Create your views here.
def index(request):
    return render(request, 'home/index.html', context={
        'title': 'Головна',
        'page': 'index',
        'app': 'home',
    })


def about(request):
    return render(request, 'home/about.html', context={
        'title': 'Про нас ',
        'page': 'about',
        'app': 'home',
    })


def book(request):
    if request.method == 'POST':
        form_name = request.POST.get('name')
        form_phone = request.POST.get('phone')
        form_email = request.POST.get('email')
        form_guests = request.POST.get('guests')
        form_date = request.POST.get('date')
        form_time = request.POST.get('time')

        BookTable.objects.create(
            name=form_name,
            phone=form_phone,   
            email=form_email,
            guests=form_guests,
            date=form_date,
            time=form_time
        )

    return render(request, 'reservations/book_table.html', context={
    'title': 'Бронювання',
    'page': 'book_table',
    'app': 'home'
    })