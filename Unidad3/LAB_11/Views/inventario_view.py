class InventarioView:
    def solicitar_datos(self):
        codigo = input("Código del producto: ").strip()
        cantidad = input("Cantidad a retirar: ").strip()
        return codigo, cantidad

    def mostrar_resultado(self, mensaje):
        print(mensaje)

    def mostrar_error(self, mensaje):
        print(mensaje)
