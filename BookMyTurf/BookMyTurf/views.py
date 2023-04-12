from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def login(request):
    pram = {'name': 'Ishan', 'location': 'INDORE'}
    return render(request, 'login.html', pram)


def bookturf(request):
    return HttpResponse("bookturf")


def service(request):
    return HttpResponse("service")


def aboutus(request):
    return HttpResponse("aboutus")


def contactus(request):
    return HttpResponse("contactus")
