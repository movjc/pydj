# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField


class Employee(models.Model):
    # employeeID = models.CharField(primary_key=True, max_length=50)
    user = models.OneToOneField(User, unique=True)
    employeeSex = models.CharField(max_length=10)
    employeeBirth = models.DateField()
    employeePhone = models.CharField(max_length=100)
    employeePlace = models.TextField()
    joinTime = models.DateField()
    isLead = models.BooleanField(default=False)

    def __unicode__(self):
        # return "Employee:%s-%s-%s" % (self.user.username, self.employeeSex, self.employeeBirth)
        return "%s" % (self.user.username,)


class Message(models.Model):
    # messageID = models.IntegerField(auto_created=True, primary_key=True)
    messageTitle = models.CharField(max_length=256)
    # messageContent = models.TextField()
    messageContent = RichTextField(config_name='default')
    employee = models.ForeignKey(Employee)
    publishTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-publishTime",)

    def __unicode__(self):
        return self.messageTitle

    def get_absolute_url(self):
        # return reverse('index', args=(self.pk,))
        return "/dailySystem/message/%i/" % self.id


class Reply(models.Model):
    # replyID = models.IntegerField(auto_created=True, primary_key=True)
    replyContent = models.TextField()
    employeeID = models.ForeignKey(Employee)
    replyTime = models.DateTimeField()
    messageID = models.ForeignKey(Message)


class Criticism(models.Model):
    # criticismID = models.IntegerField(auto_created=True, primary_key=True)
    criticismContent = models.TextField()
    employeeID = models.ForeignKey(Employee)
    criticismTime = models.DateTimeField()
    messageID = models.ForeignKey(Message)
