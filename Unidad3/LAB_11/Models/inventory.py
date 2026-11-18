from Models.products import Producto
from Models.exceptions import ProductoNoEncontrado


class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 5)
        }

    def retirar(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"El producto con código '{codigo}' no existe.")
        self.productos[codigo].retirar(cantidad)

    def obtener_stock(self, codigo):
        return self.productos[codigo].stock
