class ConfiguracionTienda:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = "Super Tienda"
            cls._instancia.impuesto = 0.16
            cls._instancia.moneda = "MXN"
        return cls._instancia


class Producto:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"
        self.configuracion = ConfiguracionTienda()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self.productos:

            if producto.tipo == "electronico":
                total += producto.precio * 1.16

            elif producto.tipo == "ropa":
                total += producto.precio * 1.08

            elif producto.tipo == "alimento":
                total += producto.precio * 1.00

        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_pedido(self):
        print(f"\n--- {self.configuracion.nombre} ---")
        print(f"Pedido #{self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Estado: {self.estado}")

        print("\nProductos:")

        for producto in self.productos:
            print(
                f"- {producto.nombre}: "
                f"${producto.precio:.2f} {self.configuracion.moneda}"
            )

        print(f"\nTotal: ${self.calcular_total():.2f} {self.configuracion.moneda}")


# main program

config1 = ConfiguracionTienda()
config2 = ConfiguracionTienda()

print(config1 is config2)

pedido = Pedido(1001, "Ana")

pedido.agregar_producto(
    Producto("Laptop", 15000, "electronico")
)

pedido.agregar_producto(
    Producto("Playera", 500, "ropa")
)

pedido.agregar_producto(
    Producto("Cereal", 100, "alimento")
)

pedido.mostrar_pedido()

pedido.cambiar_estado("ENVIADO")

print("\nNuevo estado:", pedido.estado)