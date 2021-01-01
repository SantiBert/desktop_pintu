from django.test import TestCase
from .products_methods import create_product
from .models import Product

from unittest import mock
from unittest.mock import MagicMock

class TestProductTestCase(TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        #cls.foo = Foo.objects.create(bar="Test")
        pass


    def test_create_new_product_data_ok(self):
        """
            Testeo que se pueda crear un producto correctamente
        """
        data = {
            "name": "producto1",
            "description": "New product",
            "barcode": "fjjf8812388123",
            "stocked": 12,
            "stock_type": "U",
            "last_price": 1238.30,
        }
        
        created_product = create_product(**data)
        assert created_product is not None
        assert isinstance(created_product, Product)

    def test_create_new_product_duplicated_barcode(self):
        data = {
            "name": "producto1",
            "description": "New product",
            "barcode": "fjjf8812388123",
            "stocked": 12,
            "stock_type": "U",
            "last_price": 1238.30,
        }
        mock_logging =  MagicMock()
        mock.patch("products.products_methods.logger.error", mock_logging).start()

        created_product = create_product(**data)
        created_product = create_product(**data)
        mock_logging.assert_called_once()
        mock_logging.assert_called_once_with('ERROR trying to save product - UNIQUE constraint failed: products_product.barcode')
        assert created_product is False

        
        
