from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Picture(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    sum = models.SmallIntegerField()
    result = models.SmallIntegerField()
