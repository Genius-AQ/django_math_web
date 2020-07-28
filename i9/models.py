from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    content = models.CharField(max_length=200)
    result = models.SmallIntegerField()
