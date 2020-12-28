"""Horizontal layout example."""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db_settings')
django.setup()

import sys

from app.models import Product

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
layout = QHBoxLayout()

#Product(name="Nuevo producto", bar_code="barcode2").save()
#Product(name="Nuevo producto 2 ", bar_code="barcode3").save()
#Product(name="Nuevo producto 3", bar_code="barcode1").save()


products = Product.objects.all()

tableWidget = QTableWidget()

tableWidget.setRowCount(len(products))
tableWidget.setColumnCount(2)
c = 0
for product in products:
    tableWidget.setItem(c,0, QTableWidgetItem(product.bar_code))
    tableWidget.setItem(c,1, QTableWidgetItem(product.name))
    c+=1

layout.addWidget(tableWidget)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())