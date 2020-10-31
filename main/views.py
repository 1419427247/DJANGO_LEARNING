from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
import uuid 
from .models import User

# Create your views here.

tokenDict = dict()



def userLogin(request):
    key = request.COOKIES.get('key')
    if key != None:
        if key in tokenDict:
            return tokenDict[key]
        else:
            user = User.objects.filter(token=key)
            if user:
                tokenDict[key] = user
                return user;
            else:
                r.delete_cookie('key')
                return None 

def index(request):
    user = userLogin(request)
    print(user)
    if user == None:
        return render(request,"login.html",{'msg' : 'token失效'})
    return render(request,"index.html")

def login(request):
    if request.method == "GET":
        user = userLogin(request)
        print(user)
        if user == None:
            return render(request,"login.html",{'msg' : 'token失效'})
        else:
            return redirect("/")     
    else:   
        name = request.POST.get("c_name")
        password = request.POST.get("c_password")

        ret = User.objects.filter(name=name,password=password)
        if ret:
            token = str(uuid.uuid4())
            ret.first().token = token
            ret.first().save();
            User.objects.update(token=token)
            tokenDict[token] = ret.first()
            re = redirect("/")
            re.set_cookie('key',token)
            return re;
        else:
            return render(request,"login.html",{'msg' : '用户名或密码错误'}) 



