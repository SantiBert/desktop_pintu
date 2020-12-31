from django.db import models
from products.models import Product
from app.models import Sale, Purchase


class Stock(models.Model):
    MOVEMENT_STATE =(
        ("SALE","SALE"),
        ("PURCHASE","PURCHASE"),
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField()
    movement = models.CharField(max_length=50, choices=MOVEMENT_STATE)
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, null=True)

