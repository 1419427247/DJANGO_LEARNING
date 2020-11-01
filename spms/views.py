import uuid
import base64

from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from spms.models import User,ConstructionSite

class BaseMinix(object):
    index = "index.html"
    login = "login.html"

    def is_token_valid(self,request):
        token = request.COOKIES.get('token')
        if token is None:
            return False
        else:
            user = User.objects.filter(token=token)
            if user:
                return True
        return False

    def get(self,request):
        if self.is_token_valid(request) is False:
            return render(request,self.login)
        

class Index(BaseMinix,View):
    def get(self,request):
        return super().get(request) or render(request,self.index)
    def post(self,request):
        if self.is_token_valid(request):
            if request.POST.get('type') == 'get_sites':
                r_list = []
                for site in ConstructionSite.objects.all():
                    r_list.append(site.name)
                    r_list.append(' ')
                r_list.pop();
                return HttpResponse(r_list)
            if request.POST.get('type') == 'get_sites':
                pass
class Login(BaseMinix,View):
    
    def get(self,request):
        return super().get(request) or redirect('/')

    def post(self,request):
        name = request.POST.get("user_name")
        password = request.POST.get("user_password")
        print(request.POST)
        if name is None or name == '' or password is None or password == '':
            return HttpResponse("0 请输入用户名和密码")
        ret = User.objects.filter(name=name,password=password)
        if ret.count() == 1:
            token = str(uuid.uuid1())
            ret.update(token=token)
            return HttpResponse("1 " + token)
        else:
            return HttpResponse("0 用户名或密码错误")