from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    syear = now.month == 4 and now.day == 14
    return render(request, "birthday/index.html",{
        "sinyear" : syear
    })

