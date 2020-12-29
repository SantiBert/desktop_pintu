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
    first_name = 
    last_name = 
    address = 
    phone_number = 
    email = 
    description = 
    is_client = 
    is_seller = 



class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeingKey(Someone, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class SaleProducts(models.Model):
    sale = models.ForeingKey(Sale, on_delet=models.PROTECT)
    product = models.ForeingKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField()
    quantity_type = models.CharField(choises=QUANTITY_TYPES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Purchase(models.Model):
    seller = models.ForeingKey(Someone, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
class PurchaseProduct(models.Model):
    purchase = models.ForeingKey(Purchase, on_delete=models.PROTECT)
    product = models.ForeingKey(Product, on_delete=models.PROTECT)
    traceability_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    quantity = models.FlaotField()
    quantity_type = models.CharField(choises=QUANTITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)