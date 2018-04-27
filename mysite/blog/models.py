# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('views.blog_detail', args=(self.pk,))
        return "/blog/detail/%i"  %self.id  #推荐使用这个种方法

