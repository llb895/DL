# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Comments(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    comments = models.CharField(max_length=500)
    add_time = models.DateTimeField(auto_now_add=True)


