class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    pass

class cantidadInvalida(ErrorInventario):
    pass

class stockInsuficiente(ErrorInventario):
    pass

#CLASE PRODUCTO

class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise cantidadInvalida
        if cantidad > self.stock:
            raise stockInsuficiente

    #STEP 1: VALIDATE THAT THE QUANTITYT IS GREATER THAN ZERO.
    #STEP 2: VALIDATE THAT THERE IS SUFFICIENT STOCK.
    #STEP 3: DEDUCT THE QUANTITY FROM THE STOCK

        self.stock -= cantidad


class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 5)
        }

    def retirar(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado
        self.productos[codigo].retirar(cantidad)

        #STEP 4: VERIFY THAT THE PRODUCT EXISTS
        #STEP 5: DELEGATE THE DISCOUNT TO THE PRODUCT CLASS

#PROGRAMA PRINCIPAL

def main():
    inventario = Inventario()
    codigo = input("Codigo del Producto: ")
    try:
        cantidad = int(input("Cantidad a retirar: "))
        inventario.retirar(codigo, cantidad)
        print(
            "Retiro exitoso",
            inventario.productos[codigo].stock
        )
    except ValueError:
        print("Cantidad Invalida.")
    except ErrorInventario as error:
        print("La cantidad debe ser un numero entero.")
    except ErrorInventario as error:
        print(f"No se pudo realizar la operacion: {error}")

if __name__ == "__main__":
    main()

    