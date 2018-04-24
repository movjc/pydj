# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Employee, Message
from django import forms
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib import auth
from django.shortcuts import redirect


class UserForm(forms.Form):
    employeeID = forms.CharField(label='员工号', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


@csrf_exempt
def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            employeeID = userform.cleaned_data['employeeID']
            password = userform.cleaned_data['password']

            employee = Employee.objects.filter(employeeID=employeeID, password=password)
            # employee = auth.authenticate(request, employeeID=employeeid, password=password)
            print(employee)
            if employee:
                #return redirect('index.html', permanent=True)
                #return render_to_response('index.html', {'userform': userform})
                return render(request, 'index.html')
            else:
                return HttpResponse('用户名或密码错误，请重新输入')
    else:
        userform = UserForm()
    return render_to_response('login.html', {'userform':userform})


def index(request):
    # employees = Employee.objects.all()
    messages = Message.objects.all()
    return render(request, 'index.html', {'messages': messages})


def message_list(request):
    messages = Message.objects.all()
    return render(request, 'messageList.html', {'messages': messages})


def message_detail(request, pk):
    message = Message.objects.get(pk=pk)
    # if message_slug != message.messageID:
    #     return redirect(message, permanent=True)
    return render(request, 'message.html', {'message': message})

