# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})


def blog_detail(request, article_id):
    article = BlogArticles.objects.get(id=article_id)
    print(article)
    return render(request, 'blog/detail.html', {'article': article})
