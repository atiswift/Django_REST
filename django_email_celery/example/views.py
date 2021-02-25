from django.shortcuts import render
from django.http import HttpResponse
from .task import sleepy,send_email

def index(request):
    send_email.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT</h1>')
