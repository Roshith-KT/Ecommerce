from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_account_activation_email(email, email_token):
    subject = "Family Mart Customer Account Account Activation"
    email_from = settings.EMAIL_HOST_USER
    message=f'click on the link to activate your account http://127.0.0.1:8000/credentials/activate/{email_token}'
    send_mail(subject,message,email_from,[email,])
