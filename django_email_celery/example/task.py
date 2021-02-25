from celery import shared_task
from django.core.mail import send_mail

from time import sleep
@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email():
    #sleep(2)
    send_mail('Celery Task Worked!',
        'This is the proof the task worked',
        'aditi.singh@celebaltech.com',
        ['aditusingh58@gmail.com'])
    print("hiii")
    return None
