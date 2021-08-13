from django.db import models

# Create your models here.
class DANQ(models.Model):
    output = models.CharField(max_length=600)
    hn = models.CharField(max_length=600)
    cn = models.CharField(max_length=600)
