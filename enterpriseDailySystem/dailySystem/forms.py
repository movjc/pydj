# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    employeeID = forms.CharField(label='员工号', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class MessageForm(forms.Form):
    messageTitle = forms.CharField(label='消息标题', max_length=300)
    messageContent = forms.CharField(label='消息内容', widget=forms.Textarea)
