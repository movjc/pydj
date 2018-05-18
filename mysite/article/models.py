# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class ArticleColumn(models.Model):
    user = models.ForeignKey(User,related_name="article_column")
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.column

