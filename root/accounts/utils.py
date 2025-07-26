from django.contrib.auth.tokens import default_token_generator

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def send_verification_email(request, user):
    ''' Надсилає лист підтвердження реєстрації на пошту користувача ''' 
    current_site = get_current_site(request)
    subject = 'Підтвердження реєстрації на сайті'
    # -> 
    message = render_to_string('activation/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    }) 
    # -> 
    email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    email.send()


def check_verification_token(user, token):
    ''' Перевіряє токер активації для користувача '''
    return default_token_generator.check_token(user, token)
    