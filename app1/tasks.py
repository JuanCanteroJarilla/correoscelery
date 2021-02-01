from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from djangoCelery import settings
import time

@shared_task
def send_emails_users():
    asunto = 'Mensaje de prueba de Celery'
    mensaje = 'Bienvenido esto es un mensaje de prueba con Celery, RabbitMQ y Django'
    users = User.objects.all()
    for user in users:
        time.sleep(1)
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
    return '{} se envió correo correctamente'.format(user.email)