from Controller.inventario_controller import InventarioController
from Views.inventario_view import InventarioView


def main():
    controlador = InventarioController()
    vista = InventarioView()

    codigo, cantidad = vista.solicitar_datos()
    exito, mensaje = controlador.retirar(codigo, cantidad)

    if exito:
        vista.mostrar_resultado(mensaje)
    else:
        vista.mostrar_error(mensaje)


if __name__ == "__main__":
    main()
