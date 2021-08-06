# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class information(models.Model):
    id = models.IntegerField(primary_key=True)
    factor = models.CharField(max_length=64)
    cell_line = models.CharField(max_length=500)
    ucsc = models.CharField(max_length=64)
    lab = models.CharField(max_length=500)


