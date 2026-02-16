from celery import shared_task
from time import sleep
from django.http import HttpResponse

@shared_task
def send_email():
    sleep(5)
    return print("done sent email")
