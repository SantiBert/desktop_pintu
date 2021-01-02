import pdb
import logging
from typing import List
from django.db.models import Q

from .models import Product
from .error_messages import (
    ERROR_SAVING_PRODUCT,
)

logger = logging.getLogger("django")

def create_product(
    name:str = "",
    description:str = "",
    barcode:str = None,
    stocked:float = 0,
    stock_type:str = "U",
    last_price: float = 0,
    is_active:bool=True,
    ) -> Product:
    """ Create a new product.
    Args:  
        name(str): Product name.
        barcode(str): Product barcode.

    Retruns:
        Returns a product instance if could be saved. 
        Otherwise returns false and log the error.
    """
    new_product = Product(
        name=name,
        description=description,
        barcode=barcode,
        stocked=stocked,
        stock_type=stock_type,
        last_price=last_price,
        is_active=is_active,
        )
    try:
        new_product.save()
        return new_product
    except Exception as e:
        logger.error(ERROR_SAVING_PRODUCT % str(e))
        return False


def delete_product(product_id:int, barcode:str) -> bool:    
    if product_id is not None:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            logger.error('Prodct Does Not exist')
            return False
    else:
        try:
            product = Product.objects.get(barcode=barcode)
        except Product.DoesNotExist:
            logger.error('Prodct Does Not exist')
            return False
    product.is_active = False
    product.save()


def update_product( 
    name:str = "",
    description:str = "",
    barcode:str = None,
    stocked:float = 0,
    stock_type:str = "U",
    last_price: float = 0,
    is_active:bool=True,
    ) -> Product:
    product = Product(
        name=name,
        description=description,
        barcode=barcode,
        stocked=stocked,
        stock_type=stock_type,
        last_price=last_price,
        is_active=is_active,
        )
    try:
        product.save()
        return product
    except Exception as e:
        logger.error(ERROR_SAVING_PRODUCT % str(e))
        return False


def filter_products( 
    name:str = "",
    description:str = "",
    barcode:str = None,
    is_active:bool=True,    
    ) -> List[Product]:
    """
        Filter products by the arguments.
    Args:
        name(str): Product name.
        description(str): Product description.
        barcode(str): Product barcode.
        is_active(bool): Product state.
    """  
    query_product = {}
    if name:
        query_product.update({'name__icontains': name})
    if description: 
        query_product.update({'description__icontains': description})
    if barcode:
        query_product.update({'barcode__icontains': barcode})
    products ={ Product.objects.filter(**query_product).order_by('name')}

def get_product_by_barcode(barcode:str) -> Product:
    try:
        product = Product.objects.get(barcode=barcode)
    except Product.DoesNoTExist:
        logger.error('Prodct Does Not exist')
        return False


def get_product_by_id(id:int) ->Product:
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNoTExist:
        logger.error('Prodct Does Not exist')
        return product