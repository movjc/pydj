# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Employee, Message
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib import auth
from django.shortcuts import redirect
from django import template
from .forms import UserForm, MessageForm
from django.contrib.auth.decorators import login_required


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
               # return render(request, 'index.html')
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse('用户名或密码错误，请重新输入')
    else:
        userform = UserForm()
    return render_to_response('login.html', {'userform':userform})


def index(request):
    # employees = Employee.objects.all()
    messages = Message.objects.all()
    employee = Employee.objects.get(employeeID=2)
    sex = str(employee.employeeSex)
    return render(request, 'index.html', {'messages': messages, 'employee': employee, 'sex': sex})


@login_required(login_url='login')
def message_list(request):
    """获取消息列表"""
    messages = Message.objects.all()
    return render(request, 'messageList.html', {'messages': messages})

@login_required(login_url='login')
def message_detail(request, pk):
    """获取消息详情"""
    message = Message.objects.get(pk=pk)
    # if message_slug != message.messageID:
    #     return redirect(message, permanent=True)
    return render(request, 'message.html', {'message': message})




@csrf_exempt
@login_required(login_url='login')
def message_add(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['messageTitle']
            content = form.cleaned_data['messageContent']
            #print(Title, Content)
            employeeid=1
            Message.objects.create(messageTitle=title, messageContent=content, employee_id=employeeid)
            return HttpResponseRedirect('/messageList/')
    # messageTitle = request.POST['messageTitle']
    # messageContent = request.POST['messageContent']
    else:
        form = MessageForm()

    return render(request, 'messageAdd.html', {'form': form})


ONE_PAGE_OF_DATA = 2

@login_required(login_url='login')
def message_posts(request):
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage', '1'))
        pageType = str(request.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    # 判断点击了【上一页】还是【下一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage-1)*ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = Message.objects.all()[startPos:endPos]

    if curPage == 1 and allPage ==1: # 标记1
        allPostCounts = Message.objects.count()
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    return render(request, "messagePost.html", {'posts': posts, 'allPage': allPage, 'curPage': curPage})

# 过滤器显示数据行号
register = template.Library()


@register.filter
def multiply(value, num):
    # 定义一个乘法过滤器
    return (value-1)*num









