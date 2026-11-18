"""Producto: responsabilidad única de representar un artículo y su stock."""

from exceptions import CantidadInvalida, StockInsuficiente


class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad):
        """Valida la cantidad, descuenta el stock y devuelve el stock restante."""
        # raise: si la cantidad es texto, cero, negativa o no entera, se lanza
        # CantidadInvalida y el stock queda intacto.
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise CantidadInvalida("La cantidad a retirar debe ser un entero positivo.")

        # raise: si la cantidad supera el stock disponible, se lanza
        # StockInsuficiente y no se realiza ningún descuento.
        if cantidad > self.stock:
            raise StockInsuficiente(
                "No hay suficiente stock disponible para este producto."
            )

        # Solo al pasar las dos validaciones se modifica el stock.
        self.stock -= cantidad
        return self.stock
