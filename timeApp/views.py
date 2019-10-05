from django.shortcuts import render
from .models import Visit
import datetime

def home(request):

#this will not work on exact times. a broken time function raises an error only 3 times a day

    visitor = Visit.objects 
    now =  datetime.datetime.now()
    gm = now.replace(hour=12, minute=0, second=0, microsecond=0)
    ga = now.replace(hour=18, minute=0, second=0, microsecond=0)
    ge = now.replace(hour=5, minute=45, second=0, microsecond=0)
    context = {
        'visitor' : visitor, 'time' : now
    }
    if now > ga or now < ge:
        msg = "Good Evening"
        context['msg'] = msg
    elif now > gm:
        msg = "Good Afternoon"
        context['msg'] = msg
    elif now > ge and now < gm:
        msg = "Good Morning"
        context['msg'] = msg
    else:
        msg = "time error here"
        context['msg'] = msg
    return render(request, "home.html", context)