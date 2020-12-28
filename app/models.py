from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    bar_code = models.CharField(max_length=25, unique=True)


