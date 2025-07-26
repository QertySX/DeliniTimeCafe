from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .utils import send_verification_email, check_verification_token


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', context={
            'title': 'Реєстрація',
            'page': 'signup',
            'app':'accounts',
        })
    elif request.method == 'POST':
        # -> 
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')
        # -> 
        user = User.objects.create_user(login_x, email_x, pass1_x)

        # -> 
        if user is None:
            color = 'red'
            message = 'Не вдалось зберігти дані користувача у базу'
        else:
            # 4 - Робота із Email
            user.is_active = False
            user.save()
            send_verification_email(request, user)

            # ->
            color = 'green'
            message = 'Будь ласка перевірте свою пошту, щоб завершити реєстрацію'

        return render(request, 'accounts/report.html', context={
            'title': 'Звіт про реєстрацію',
            'page': 'report',
            'app': 'accounts',
            'color': color,
            'message': message
        })  
            
        
def signin(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html', context={
            'title': 'Логін',
            'page': 'signin',
            'app':'accounts',
        })
    elif request.method == 'POST':
        # -> 
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        # -> 
        user = authenticate(request, username=login_x, password=pass1_x)
        # -> 
        if user is not None:
            login(request, user)
            color = 'green'
            message = 'Авторизація успішна'
        # - Користувач не знайдений або не активний
        else:
            try:
                potential_user = User.objects.get(username=login_x)
            except User.DoesNotExist:
                potential_user = None

            # - Користувач знайдений, але не активний:
            if potential_user is not None and not potential_user.is_active:
                color = 'red'
                message = 'Ваш акаунт не активовано!'
            # - Користувач не знайдений: 
            else:
                color = 'red'
                message = 'Ваш акаунт не активований!'

        return render(request, 'accounts/report.html', context={
            'title': 'Звіт про авторизацію',
            'page': 'report',
            'app': 'accounts',
            'color': color,
            'message': message
        })  


def signout(request):
    logout(request)
    return redirect('index')


def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль',
        'page': 'profile',
        'app': 'accounts',
    })


def ajaxreg(request):
    response = dict()
    login_y = request.GET.get('login')

    # ->
    try:
        User.objects.get(username=login_y)
        response['message'] = 'Логін - зайнятий!'
    except User.DoesNotExist:
        response['message'] = 'Логін - вільний!'
    # ->
    return JsonResponse(response)


def activate(request, uidb64, token):
    ''' Обробляє запит з пошти користувача на активацію '''
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # -> 
    if user is not None and check_verification_token(user, token):
        user.is_active = True
        user.save()
        message = 'Ваш обліковий запис успішно активовано'
        color = 'green'
    else:
        message = 'Посилання для активації не дійсне!'
        color = 'red'
    # ->
    return render(request, 'accounts/report.html', context={
            'title': 'Звіт про активацію',
            'page': 'report',
            'app': 'accounts',
            'color': color,
            'message': message
        }) 