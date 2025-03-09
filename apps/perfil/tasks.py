from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def enviar_correo_reset_password(email, subject, message):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
