# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from browse.models import information


@require_http_methods(["GET"])
def show_information(request):
    response = {}
    try:
        a = information.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", a))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
