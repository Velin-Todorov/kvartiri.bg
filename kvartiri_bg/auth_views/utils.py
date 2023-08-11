from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token

def activateEmail(request, user):
        mail_subject = 'Activate your user account'
        message = render_to_string(
            'auth_templates/email_activate_acc.html',
            {
                'user': user.email,
                'domain': f'{request.get_host()}',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
        )
        email = EmailMessage(mail_subject, message, to=[user.email])
        if email.send():
            messages.success(
                request,
                f'A verification email has been sent to the provided email. Click on it to complete your registration'
            )
        
        else:
            messages.error(request, f'Problem sending email to {user.email}, check if you typed it correctly.')

