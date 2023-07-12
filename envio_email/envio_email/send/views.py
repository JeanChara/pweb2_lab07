from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    
    send_mail('Hello from Django',
    'Hello there. This is an automated message.',
    'jean13@gmail.com',
    ['jcharaco@unsa.edu.pe'],
    fail_silently=False)

    return render(request, 'send/index.html')
