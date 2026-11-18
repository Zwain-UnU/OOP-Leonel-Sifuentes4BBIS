from Models.inventory import Inventario
from Models.exceptions import ErrorInventario


class InventarioController:
    def __init__(self):
        self.inventario = Inventario()

    def retirar(self, codigo, cantidad):
        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            return False, "La cantidad debe ser un número entero."

        try:
            self.inventario.retirar(codigo, cantidad)
        except ErrorInventario as error:
            return False, f"No se pudo realizar la operación: {error}"

        stock = self.inventario.obtener_stock(codigo)
        return True, f"Retiro realizado. Stock restante: {stock}"
