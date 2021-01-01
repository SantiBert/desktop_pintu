import pdb
import logging
from typing import List


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
    """
        Delete a product by an id or by a barcode. This is a logical delete, 
        change the is_active value to false.
    Args: 
        product_id(int): Product id.
        barcode(str): Product barcode.

    Returns :
        True if could be deleted. 
        False if there was an error and log the error.
    """
    pass


def update_product( 
    name:str = "",
    description:str = "",
    barcode:str = None,
    stocked:float = 0,
    stock_type:str = "U",
    last_price: float = 0,
    is_active:bool=True,
    ) -> Product:
    pass


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
    pass


def get_product_by_barcode(barcode:str) -> Product:
    """
        Get a product by a barcode.
    Args:
        barcode(str): Barcode product to search.
    """
    pass


def get_product_by_id(id:int) ->Product:
    """
        Get a product by a product id.
    Args:
        id(int): Product id to get.
    """
    pass