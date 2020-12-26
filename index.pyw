from tkinter import *
from tkinter import ttk
import sqlite3


class Products:
    db_name = 'database.db'

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
        Label(frame, text='Precio: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Ingresa el stock
        Label(frame, text='Stock: ').grid(row=3, column=0)
        self.stock = Entry(frame)
        self.stock.grid(row=3, column=1)

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
        self.tree.heading('#1', text='Precio', anchor=CENTER)
        self.tree.heading('#2', text='Stock', anchor=CENTER)

        # Boton para borrar productos
        ttk.Button(text='Borrar', command=self.delete_product).grid(
            row=5, column=0, sticky=W + E)
        ttk.Button(text='Editar', command=self.edit_product).grid(
            row=5, column=1, sticky=W + E)

        self.get_products()

    # crea las busqueda a la base de datos

    def run_query(self, query, parameters=()):
        with sqlite3 .connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
            return result

    # Permite obtener la lista de productos desde la base de datos
    def get_products(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_row = self.run_query(query)
        for row in db_row:
            self.tree.insert(
                '', 0, text=row[1], values=(row[2], row[3]))

    # Valida un nuevo producto con precio y nombre
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    # Agregua un nuevo producto
    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?, ?)'
            parameters = (self.name.get(), self.price.get(), self.stock.get())
            self.run_query(query, parameters)
            self.message['text'] = 'El producto {} ha sido agregado exitosamente'.format(
                self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
            self.stock.delete(0, END)
        else:
            self.message['text'] = 'Nombre y precio requerido requerido'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor seleccione un producto'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text'] = 'El producto {} ha sido eliminado exitosamente'.format(
            name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor seleccione un producto'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        old_stock = self.tree.item(self.tree.selection())['values'][1]
        self.edit_wind = Toplevel()
        self.edit_wind.title = "Editar producto"
        # Nombre anterior
        Label(self.edit_wind, text='Nombre anterior: ').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
                                                     value=name), state='readonly').grid(row=0, column=2)
        # Nombre nuevo
        Label(self.edit_wind, text='Nombre Nuevo: ').grid(row=1, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1, column=2)

        # Precio anterior
        Label(self.edit_wind, text='Precio anterior: ').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
                                                     value=old_price), state='readonly').grid(row=2, column=2)
        # Precio nuevo
        Label(self.edit_wind, text='Precio Nuevo: ').grid(row=3, column=1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row=3, column=2)

        # Stock anterior
        Label(self.edit_wind, text='Stock anterior: ').grid(row=4, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
                                                     value=old_stock), state='readonly').grid(row=4, column=2)

        # Stock nuevo
        Label(self.edit_wind, text='Stock Nuevo: ').grid(row=5, column=1)
        new_stock = Entry(self.edit_wind)
        new_stock.grid(row=5, column=2)
        Button(self.edit_wind, text='Aceptar', command=lambda: self.change_elements(
            new_name.get(), name, new_price.get(), old_price, new_stock.get(), old_stock)).grid(row=6, column=2, sticky=W)
        self.edit_wind.mainloop()

    def change_elements(self, name, new_name, new_price, new_stock, old_price, old_stock):
        query = 'UPDATE product SET name = ?, price = ?, stock = ? WHERE name = ? AND price = ? AND stock = ?'
        parameters = (new_name, new_price,
                      new_stock, name, old_price, old_stock)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'El producto {} ha sido editado exitosamente'.format(
            name)
        self.get_products()


if __name__ == '__main__':
    window = Tk()
    application = Products(window)
    window.mainloop()
