import os
from datetime import datetime

from Models.products_model import Producto
from exporters import ExportadorCSV, ExportadorTXT, ExportadorJSON, ExportadorPDF


class ProductoController:
    """Coordina el Modelo de productos con el módulo de exportadores (Patrón Strategy)."""

    FORMATOS_EXPORTACION = {
        "CSV": (ExportadorCSV, ".csv"),
        "TXT": (ExportadorTXT, ".txt"),
        "JSON": (ExportadorJSON, ".json"),
        "PDF": (ExportadorPDF, ".pdf"),
    }

    def __init__(self):
        self.modelo = Producto()

    def obtener_productos(self):
        """Solicita al Modelo la lista completa de productos registrados."""
        return self.modelo.obtener_todos()

    def generar_reporte(self, formato):
        """Instancia la subclase Exportador correspondiente al formato elegido
        y ejecuta exportar() de forma polimórfica."""
        formato = formato.upper()

        if formato not in self.FORMATOS_EXPORTACION:
            return False, f"El formato '{formato}' no es soportado."

        datos = self.obtener_productos()
        if not datos:
            return False, "No hay productos registrados para exportar."

        clase_exportadora, extension = self.FORMATOS_EXPORTACION[formato]

        directorio_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        marca_de_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta_archivo = os.path.join(directorio_raiz, f"reporte_productos_{marca_de_tiempo}{extension}")

        exportador = clase_exportadora()
        try:
            exportador.exportar(datos, ruta_archivo)
        except Exception as error:
            return False, f"Ocurrió un error al generar el archivo: {error}"

        return True, ruta_archivo
