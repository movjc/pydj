# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    nid = models.AutoField(primary_key=True)  # 自增id(可以不写，默认会有自增id)
    title = models.CharField(max_length=32)
    publishDdata = models.DateField()  # 出版日期
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 一共5位，保留两位小数

    #一个出版社有多本书，关联字段要写在多的一方
    # 不用命名为publish_id，因为django为我们自动就加上了_id
    publish = models.ForeignKey("Publish")  #foreignkey（表名）建立的一对多关系
    # publish是实例对象关联的出版社对象
    authorlist = models.ManyToManyField("Author")  #建立的多对多的关系

    def __unicode__(self):  #__str__方法使用来吧对象转换成字符串的，你返回啥内容就打印啥
        return self.title


class Publish(models.Model):
    #不写id的时候数据库会自动给你增加自增id
    name =models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()


class AuthorDeital(models.Model):
    tel = models.IntegerField()
    addr = models.CharField(max_length=32)
    author = models.OneToOneField("Author")  #建立的一对一的关系