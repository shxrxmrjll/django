from django.shortcuts import render
from emaill.settings import EMAIL_HOST_USER
from . import forms 
from django.core.mail import send_mail

# Create your views here.

def obuna(request):
    o = forms.Emailapp()
    if request.method == 'POST':
        o = forms.Emailapp(request.POST)
        subject = 'Obuna Bo`ldingiz'
        message = 'Obuna bo`ldingiz!!!  Kartangizdan 1 000 000 UZS muvaffaqiyatli yechildi. RAXMAT!!!'
        recepient = str(o['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':o})
