"""Excepciones personalizadas del sistema de inventario (SRP: solo errores)."""


class ErrorInventario(Exception):
    """Clase base: toda excepción del inventario hereda de aquí."""

    pass


class ProductoNoEncontrado(ErrorInventario):
    """Se lanza cuando el código del producto no existe en el inventario."""

    pass


class CantidadInvalida(ErrorInventario):
    """Se lanza cuando la cantidad a retirar no es un entero positivo."""

    pass


class StockInsuficiente(ErrorInventario):
    """Se lanza cuando la cantidad solicitada supera el stock disponible."""

    pass
