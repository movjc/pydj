# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import ArticleColumn
from .forms import ArticleColumnForm, ArticlePostForm


@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    """新增栏目"""
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request, "article/column/article_column.html", {"columns": columns, "column_form": column_form})

    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)  # 查询添加的栏目是否存在，
        print(columns)
        if columns:  # 如果存在columns有内容 则返回2
            return HttpResponse("2")
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("1")


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def rename_article_column(request):
    """栏目重名名"""
    column_name = request.POST['column_name']
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)  # 根据栏目id，查询数据
        line.column = column_name  # 重新给栏目赋值
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_article_column(request):
    """删除栏目"""
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


@login_required(login_url='/account/login/')
@csrf_exempt
def article_post(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return render(request, "article/column/article_post.html", {"article_post_form": article_post_form, "article_columns":article_columns})