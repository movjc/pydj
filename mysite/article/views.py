# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import ArticleColumnForm


@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    columns = ArticleColumn.objects.filter(user=request.user)
    return render(request, "article/column/article_column.html", {"columns": columns})
    # if request.method == "GET":
    #     columns = ArticleColumn.objects.filter(user=request.user)
    #     column_form = ArticleColumnForm()
    #     return render(request, "article/column/article_column.html", {"columns": columns, "column_form": column_form})
    # if request.method == "POST":
    #     column_name = request.POST['column']
    #     columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
    #     if columns:
    #         return HttpResponse("2")
    #     else:
    #         ArticleColumn.objects.filter(user=request.user, column=column_name)
    #         return HttpResponse("1")

