from inventory import Inventario
from exceptions import ErrorInventario

def main():
    inventario = Inventario()
    codigo = input("Código del producto: ")
    try:
        cantidad = int(input("Cantidad a retirar: "))
        inventario.retirar(codigo, cantidad)
        print(
            "Retiro realizado. Stock restante: ",
            inventario.productos[codigo].stock
        )
        
    except ValueError:
        print("La cantidad debe ser un número entero.")
    except ErrorInventario as error:
        print(f"No se pudo realizar la operación: {error}")
        
if __name__ == "__main__":
    main()