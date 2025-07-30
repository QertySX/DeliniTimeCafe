from django.shortcuts import render, redirect
from .models import BookTable, Reviews
from django.contrib.auth.decorators import login_required


def index(request):
    reviews = Reviews.objects.all()
    user_reviews = Reviews.objects.filter(user_id=request.user.id)
    return render(request, 'home/index.html', context={
        'title': 'Головна',
        'page': 'index',
        'app': 'home',
        'reviews': reviews,
        'user_reviews': user_reviews
    })


def about(request):
    return render(request, 'home/about.html', context={
        'title': 'Про нас ',
        'page': 'about',
        'app': 'home',
    })


@login_required(login_url='signin')
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


@login_required(login_url='signin')
def add_reviews(request):
    if request.method == 'GET':
        return render(request, 'home/add_reviews.html', context={
        'title': 'Відгуки',
        'page': 'add_reviews',
        'app': 'home',
        })
    elif request.method == 'POST':
        try:
            rating = int(request.POST.get('rating'))
            text = request.POST.get('text')
            add = Reviews.objects.create(
                user=request.user,
                rating=rating,
                text=text
            )
            return redirect('index')
        except Exception as e:
            print(f'Ошибка: {e}')
            return render(request, 'home/add_reviews.html', {
            'error': 'Помилка при збереженні відгуку.',
            'title': 'Відгуки',
            'page': 'add_reviews',
            'app': 'home',
        })


@login_required(login_url='signin')
def del_review(request, reviews_id):
    delete_review = Reviews.objects.get(id=reviews_id)
    if request.user == delete_review.user:
        delete_review.delete()
        return redirect('index')


@login_required(login_url='signin')
def edit_review(request, reviews_id):
    if request.method == 'GET':
        return render(request, 'home/edit_reviews.html', context={
            'title': 'Змінити відгук',
            'page': 'edit_reviews',
            'app': 'home',
            })
    elif request.method == 'POST':
        edit_rating = request.POST.get('rating')
        edit_text = request.POST.get('text')

        edit_rev = Reviews.objects.get(id=reviews_id)
        if request.user == edit_rev.user:
            edit_rev.rating = edit_rating
            edit_rev.text = edit_text
            edit_rev.save()
            return redirect('index')