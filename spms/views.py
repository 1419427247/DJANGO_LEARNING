import uuid
import base64
import json
from django.db import models
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import redirect, render
from django.views import View
from django.template import Template
from spms.models import User, Worker, ConstructionSite


class LoginDecorator(object):
    def __call__(self, func):
        def decorated(*args, **kwargs):
            token = args[1].COOKIES.get('token')
            if userManager.isLogged(token):
                return func(*args, **kwargs)
            else:
                return redirect("/login")
        return decorated

class ModelManager(object):
    def to_string(self,objects,*args):
        if objects is None:
            return ''
        arr = []
        for obj in objects:
            kv_dice = dict()
            for arg in args:
                kv_dice[arg] = getattr(obj,arg)
            arr.append(kv_dice)
        return json.dumps(arr)

class UserManager():
    def isLogged(self, token):
        if token is not None and User.objects.filter(token=token).exists():
            return True
        else:
            return False

class ConstructionSiteManager(ModelManager):
    def get_all(self):
        sites = ConstructionSite.objects.all()
        return self.to_string(sites,'id','name','address')

class WorkerManager(ModelManager):
    def get_all_by_site_id(self,value):
        workers = Worker.objects.filter(site_id=value)
        return self.to_string(workers,'id','name','sex','id_number','residential_address')

userManager = UserManager()
constructionSiteManager = ConstructionSiteManager()
workerManager = WorkerManager()





class Index(View):
    @LoginDecorator()
    def get(self,request):
        return render(request,"index.html")

    @LoginDecorator()
    def post(self, request):
        if request.POST.get('type') == 'get_sites':
            return HttpResponse(constructionSiteManager.get_all())

        elif request.POST.get('type') == 'get_workers':
            site_id = request.POST.get('site_id')
            return HttpResponse(workerManager.get_all_by_site_id(site_id),content_type = "application/json")

        elif request.POST.get('type') == 'search_workers':
            search_id = request.POST.get('search_id')
            search_name = request.POST.get('search_name')
            search_id_number = request.POST.get('search_id_number')
            if search_id != '':
                workers = Worker.objects.filter(id=search_id)
            else:
                workers = Worker.objects.filter(
                    name__contains=search_name, id_number__contains=search_id_number)
            worker_list = ['']
            for worker in workers:
                worker_list.append(worker.id)
                worker_list.append(' ')
                worker_list.append(worker.name)
                worker_list.append(' ')
                worker_list.append(worker.sex)
                worker_list.append(' ')
                worker_list.append(worker.id_number)
                worker_list.append(' ')
                worker_list.append(worker.residential_address)
                worker_list.append(' ')
            worker_list.pop()
            return HttpResponse(worker_list)

class Login(View):
    
    def get(self, request):
        if userManager.isLogged(request.COOKIES.get('token')):
            return redirect("/")
        return render(request,"login.html")

    def post(self, request):
        name = request.POST.get("user_name")
        password = request.POST.get("user_password")
        if name is None or name == '' or password is None or password == '':
            return HttpResponse("0 请输入用户名和密码")
        ret = User.objects.filter(name=name, password=password)
        if ret.count() == 1:
            token = str(uuid.uuid1())
            ret.update(token=token)
            response = HttpResponse("1 " + token)
            response.set_cookie("token",token)
            return response
        else:
            return HttpResponse("0 用户名或密码错误")
