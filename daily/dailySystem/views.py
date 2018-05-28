# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Message, Employee
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .forms import SendMessageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    messages = Message.objects.all()[:5]
    return render(request, 'index.html', {'messages': messages})


# @login_required(login_url='/dailySystem/login')
# # def message_list(request):
# #     """获取消息列表"""
# #     messages = Message.objects.all()
# #     return render(request, 'messageList.html', {'messages': messages})


@login_required(login_url='/dailySystem/login')
def message_detail(request, pk):
    """获取消息详情"""
    message = Message.objects.get(pk=pk)
    user = User.objects.get(username=request.user.username)
    return render(request, 'message.html', {'message': message, 'user': user})


@csrf_exempt
@login_required(login_url='/dailySystem/login')
def message_add(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user = User.objects.get(username=request.user.username)
            Message.objects.create(messageTitle=title, messageContent=content, employee_id=user.id)
            return HttpResponseRedirect('/dailySystem/messageList/')
    else:
        form = SendMessageForm()

    return render(request, 'messageAdd.html', {'form': form})


@login_required(login_url='/dailySystem/login')
def message_list(request):
    limit = 5  # 每页显示记录数
    messages = Message.objects.all()
    paginator = Paginator(messages, limit)  # 实例化分页对象

    page = request.GET.get('page')  # 获取页码

    try:
        messages = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是整数
        messages = paginator.page(1)  # 获取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        messages = paginator.page(paginator.num_pages)  # 获取最后一页数据
    print(messages)
    return render(request, 'messageList.html', {'messages': messages})
