# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from models import UserApp
from django.views.decorators.csrf import csrf_exempt,csrf_protect #出现csrf 403的时候，需要添加这个，然后在函数前面加装饰器

# Create your views here.
class UserForm(forms.Form):

    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.CharField(label='邮箱', max_length=100)

@csrf_exempt
def regist(request):
    if request.method =='POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            k = UserApp.objects.create(username=username, password=password, email=email)
            k.save()

            return HttpResponse('regist success')
    else:
        userform = UserForm()
    return render_to_response('regist.html', {'userform':userform})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = UserApp.objects.filter(username__exact=username,password__exact=password)

            if user:
                return render_to_response('index.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render_to_response('login.html',{'userform':userform})
