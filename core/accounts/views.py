from django.shortcuts import render
from .tasks import send_email
from django.http import HttpResponse
# Create your views here.

def send_email(request):
    send_email.delay()
    return HttpResponse("<h1> Email is being sent </h1>")