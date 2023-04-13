from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def bookturf(request):
    return render(request, 'bookturf.html')


def service(request):
    return render(request, 'service.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')
