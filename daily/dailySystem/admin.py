# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Employee,Message


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("user", "employeeSex", "employeeBirth", "employeePlace", "joinTime", "isLead")
    list_filter = ("user", "joinTime")
    ordering = ['joinTime']


class MessageAdmin(admin.ModelAdmin):
    list_display = ("messageTitle", "messageContent", "publishTime", "employee_id")
    list_filter = ("publishTime",)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Message, MessageAdmin)
