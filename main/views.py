from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    print(request.COOKIES)
    return render(request,"index.html")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")    
    else:   
        n = request.POST.get("c_name")
        p = request.POST.get("c_password")

        re = redirect("/");
        re.set_cookie('key',123);
        return re;




