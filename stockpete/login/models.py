from __future__ import unicode_literals

from django.db import models

class Login(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
# Create your models here.

