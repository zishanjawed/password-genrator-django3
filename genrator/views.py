from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'genrator/home.html')
def about(request):
    return render(request,'genrator/about.html')

def password(request):
    thepassword=''
    charector=list('abcdefghijklmnopqrstuvwxyz')
    lenght=int(request.GET.get('lenght',12))
    if request.GET.get('uppercase'):
        charector.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        charector.extend(list('0123456789'))
    if request.GET.get('special'):
        charector.extend(list('!@#$%^&*+_'))


    for x in range(lenght):
        thepassword += random.choice(charector)

    return render(request, 'genrator/password.html',{"password":thepassword})
