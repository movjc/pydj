# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Employee, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("messageID", "messageTitle", "messageContent", "publishTime", "employee_id")
    list_filter = ("publishTime",)

admin.site.register(Employee)
admin.site.register(Message,MessageAdmin)
