from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
import uuid 
from .models import User,Worker

# Create your views here.

tokenDict = dict()

def userLogin(request,template):
    if haslogged(request) == True:
        return render(request,template)
    re = render(request,"login.html")
    re.delete_cookie('key')
    return re

def haslogged(request):
    key = request.COOKIES.get('key')
    print(key)
    if key in tokenDict:
        return True
    else:
        user = User.objects.filter(token=key)
        if user:
            tokenDict[key] = user
            return True;        
    return False

def index(request):
    return userLogin(request,"index.html")

def login(request):
    if request.method == "GET":
        return userLogin(request,"login.html")
    else:   
        name = request.POST.get("c_name")
        password = request.POST.get("c_password")

        ret = User.objects.filter(name=name,password=password)
        if ret:
            token = str(uuid.uuid4())
            ret.first().token = token
            ret.update(token=token)
            tokenDict[token] = ret.first()
            re = redirect("/")
            re.set_cookie('key',token)
            return re;
        else:
            return render(request,"login.html",{'msg' : '用户名或密码错误'}) 

def search(request):
    if haslogged(request) == False:
        return render(request,"login.html")
    id = request.GET.get('id')
    # name = request.GET.get('name')
    # sex = request.GET.get('sex')

    workers = Worker.objects.all().filter(id=id)
    if workers.count() == 0:
        return HttpResponse("没有找到相关的员工信息")

    str = "";
    for worker in workers:
        str += "姓名:" + worker.name + "   性别:" + worker.sex + "    身份证号:" + worker.id_number + "</br>"

    return HttpResponse(str)