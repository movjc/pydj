# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Blog
from django.shortcuts import render_to_response
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def  index(request):
    blog_list = Blog.objects.all()
    template = loader.get_templat('blog/index.html')
    context = {
        'blog_list': blog_list,
    }
    return HttpResponse(template.render(context,request))
