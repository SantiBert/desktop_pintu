import uuid

from django.db import models


class Product(models.Model):    
    name = models.CharField(max_length=200)
    bar_code = models.CharField(max_length=25, unique=True)
    stock_quantity = models.FloatField()
    last_price = models.Float


class ProductPrices(models.Model):
    product = models.ForeingKey(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
