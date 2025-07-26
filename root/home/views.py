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
            user=request.user,
            name=form_name,
            phone=form_phone,   
            email=form_email,
            guests=form_guests,
            date=form_date,
            time=form_time
        )
        return redirect('done')

    return render(request, 'reservations/book_table.html', context={
    'title': 'Бронювання',
    'page': 'book_table',
    'app': 'home',
    'user_reserved': BookTable.objects.filter(user_id=request.user.id)
    })


def done(request):
    return render(request, 'reservations/done.html', context={
    'title': 'Бронювання успішне',
    'page': 'done',
    'app': 'home',
    'user_reserved': BookTable.objects.filter(user_id=request.user.id)
    })


def del_reserv(request, book_table_id):
    delete_reserv = BookTable.objects.get(id=book_table_id)
    delete_reserv.delete()
    return redirect('book_table')