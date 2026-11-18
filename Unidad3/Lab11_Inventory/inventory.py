"""Inventario: responsabilidad única de registrar y localizar productos."""

from exceptions import ProductoNoEncontrado
from products import Producto


class Inventario:
    def __init__(self):
        # Se agregan dos productos nuevos con códigos y stocks distintos.
        self.productos = {
            "P01": Producto("P01", 5),
            "P02": Producto("P02", 10),
            "P03": Producto("P03", 3),
        }

    def retirar(self, codigo, cantidad):
        """Busca el producto y delega el retiro; no captura sus excepciones."""
        # raise: si el código no está registrado, se lanza ProductoNoEncontrado.
        if codigo not in self.productos:
            raise ProductoNoEncontrado(
                f"El producto con código '{codigo}' no existe."
            )

        # Las excepciones de Producto.retirar() se propagan hasta main().
        return self.productos[codigo].retirar(cantidad)

    def obtener_stock(self, codigo):
        return self.productos[codigo].stock
