# -*- coding: utf-8 -*-
from django import forms


class SendMessageForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
