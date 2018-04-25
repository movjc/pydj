# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Employee(models.Model):
    employeeID = models.CharField(primary_key=True, max_length=50)
    employeeName = models.CharField(max_length=256)
    employeeSex = models.CharField(max_length=10)
    employeeBirth = models.DateField()
    employeePhone = models.CharField(max_length=100)
    employeePlace = models.TextField()
    joinTime = models.DateField()
    password = models.CharField(max_length=256)
    isLead = models.BooleanField(default=False)

    def __unicode__(self):
        return self.employeeName


class Message(models.Model):
    messageID = models.IntegerField(auto_created=True, primary_key=True)
    messageTitle = models.CharField(max_length=256)
    messageContent = models.TextField()
    employee = models.ForeignKey(Employee)
    publishTime = models.DateTimeField()

    # def __unicode__(self):
    #     return  self.employeeID  #,  self.messageTitle,

    # def get_absolute_url(self):
    #     return reverse('message', args=(self.pk, self.messageID,))


class Reply(models.Model):
    replyID = models.IntegerField(auto_created=True, primary_key=True)
    replyContent = models.TextField()
    employeeID = models.ForeignKey(Employee)
    replyTime = models.DateTimeField()
    messageID = models.ForeignKey(Message)


class Criticism(models.Model):
    criticismID = models.IntegerField(auto_created=True, primary_key=True)
    criticismContent = models.TextField()
    employeeID = models.ForeignKey(Employee)
    criticismTime = models.DateTimeField()
    messageID = models.ForeignKey(Message)