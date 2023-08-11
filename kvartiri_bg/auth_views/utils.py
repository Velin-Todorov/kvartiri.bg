from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
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

