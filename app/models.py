import uuid


from django.db import models
from django.contrib.auth.models import User

from products.models import Product


QUANTITY_TYPES = (
    ("Kilogramo/s","Kilogramo/s"),
    ("Litro/s", "Litro/s"),
    ("Unidad/es", "Unidad/es"),
    ("Centimetros", "Centimetros"),
    )

class Someone(models.Model):
    first_name = models.CharField(max_length= 150)
    last_name = models.CharField(max_length= 150)
    address = models.CharField(max_length= 150)
    phone_number = models.CharField(max_length= 20)
    email = models.EmailField( max_length=254)
    description = models.TextField()
    is_client = models.BooleanField(default= False)
    is_seller = models.BooleanField(default= False)



class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Someone, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class SaleProducts(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField()
    quantity_type = models.CharField(choices=QUANTITY_TYPES,max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Purchase(models.Model):
    seller = models.ForeignKey(Someone, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField()
    quantity_type = models.CharField(choices=QUANTITY_TYPES, max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)