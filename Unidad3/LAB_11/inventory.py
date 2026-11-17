from products import Producto
from exceptions import ProductoNoEncontrado


class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 5)
        }

    def retirar(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"El producto con código '{codigo}' no existe.")
        self.productos[codigo].retirar(cantidad)
