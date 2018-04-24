# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    string = u'我在自学Django,准备用来重新做公司官网' #显示字符串
    '''
     #一般的变量之类的用 {{ }}（变量），功能类的，比如循环，条件判断是用 {%  %}（标签）
    '''
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    #在模板进行 条件判断和 for 循环的详细操作
    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'home.html', {'List': List})


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
