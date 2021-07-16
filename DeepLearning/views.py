# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from DeepLearning.models import Comments


# Create your views here.
# add_book接受一个get请求，往数据库里添加一条book数据
@require_http_methods(["GET"])
def submitcomment(request):
    response = {}
    try:
        information = Comments(name = request.GET.get('name'),email = request.GET.get('email'),comments = request.GET.get('comments'))
        information.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# show_books返回所有的书籍列表（通过JsonResponse返回能被前端识别的json格式数据）
@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Comments.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
