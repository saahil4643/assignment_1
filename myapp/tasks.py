from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    try:
        send_mail(
            'Welcome!',
            'Thanks for registering, welcome to our site!',
            'sahilbhandare80@gmail.com',  # This can be anything for now
            [email],
            fail_silently=False,
        )
        return "Email sent"
    except Exception as e:
        return str(e)
