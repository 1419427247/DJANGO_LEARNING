from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    users=User.objects.all()
    l=list();
    for i,user in enumerate(users):
        l.append("{}.".format(str(i))+str(user)+"<br>")
    return HttpResponse(l)
