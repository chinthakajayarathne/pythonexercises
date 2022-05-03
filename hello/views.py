from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Hello World !!!")


def sam(request):
    return HttpResponse("Hello sam !!!")


def dan(request):
    return HttpResponse("Hello dan !!!")


def mam(request):
    return HttpResponse("Hello mam !!!")


def sunil(request):
    return render(request, "hello/sunil.html")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.upper()
    })
