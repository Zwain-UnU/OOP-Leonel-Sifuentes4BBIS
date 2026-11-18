"""Programa principal: responsabilidad única de E/S y manejo de excepciones."""

from exceptions import ErrorInventario
from inventory import Inventario


def main():
    inventario = Inventario()

    codigo = input("Código del producto: ").strip()
    cantidad_texto = input("Cantidad a retirar: ").strip()

    try:
        # ValueError: int() falla si el usuario escribe texto en vez de un número.
        cantidad = int(cantidad_texto)

        # ErrorInventario captura ProductoNoEncontrado, CantidadInvalida y
        # StockInsuficiente por herencia; las excepciones se propagan desde
        # Producto e Inventario hasta este nivel.
        stock_restante = inventario.retirar(codigo, cantidad)
    except ValueError:
        # except: maneja la entrada no numérica del usuario.
        print("Error: La cantidad debe ser un número entero.")
    except ErrorInventario as error:
        # except: maneja cualquier error de inventario con su mensaje propio.
        print(f"Error: {error}")
    else:
        # else: solo se ejecuta si el bloque try terminó sin excepciones.
        print(f"Retiro exitoso. Stock restante: {stock_restante}")


if __name__ == "__main__":
    main()
