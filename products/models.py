import uuid

from django.db import models


class Product(models.Model):
    STOCK_TYPE = (
        ("KG", "KG"),
        ("MTS", "MTS"),
        ("LTS", "LTS"),
        ("U", "U"),
        ("M2","M2"),
    )    
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=25, unique=True)
    stocked = models.FloatField()
    stock_type = models.CharField(max_length=20, choices=STOCK_TYPE)
    last_price = models.FloatField()
    is_active = models.BooleanField(default=True)
    #qr = models.ImageField()


class ProductPrices(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost =  models.DecimalField(max_digits=10, decimal_places=2)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()    
    is_active = models.BooleanField(default=True)
