from tkinter import *
from tkinter import ttk
import sqlite3
from app.models import Product

class Products:
 

    def __init__(self, window):
        self.wind = window
        self.wind.title('Productos')
        # self.wind.geometry('750x450')
        self.wind.resizable(0, 0)

        # Registra un producto nuevo
        frame = LabelFrame(self.wind, text='Ingresar un preducto nuevo')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Ingresa el nombre
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Ingresa el precio
        Label(frame, text='Stock: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Boton de guardar producto
        ttk.Button(frame, text='Guardar producto', command=self.add_product).grid(
            row=4, columnspan=2, sticky=W+E)

        # Mensaje de producto agregado
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Tabla
        self.tree = ttk.Treeview(
            height=8, columns=("#1", "#2"))
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
    

        # Boton para borrar productos
        ttk.Button(text='Borrar', command=self.delete_product).grid(
            row=5, column=0, sticky=W + E)
        ttk.Button(text='Editar', command=self.edit_product).grid(
            row=5, column=1, sticky=W + E)

        self.get_products()

    
    # Permite obtener la lista de productos desde la base de datos
    def get_products(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        products = Product.objects.all()
        for product in products:
            self.tree.insert('', 0,  values=(product.name))

    # Agregua un nuevo producto
    def add_product(self):
        Product(name=self.name.get()).save()
        self.message['text'] = 'El producto {} ha sido agregado exitosamente'.format(
            self.name.get())
        self.name.delete(0, END)
        self.price.delete(0, END)
        self.stock.delete(0, END)
        
        self.get_products()
    


if __name__ == '__main__':
    window = Tk()
    application = Products(window)
    window.mainloop()
