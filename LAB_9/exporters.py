import csv
import json
from fpdf import FPDF


class Exportador:
    def exportar(self, datos, ruta_archivo):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class ExportadorTXT(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in datos:
                # El Modelo retorna diccionarios: {'id', 'nombre', 'precio', 'stock'}
                file.write(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Stock: {producto['stock']}\n")
        print(f"Archivo TXT generado en: {ruta_archivo}")


class ExportadorCSV(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerow(["ID", "Nombre", "Precio", "Stock"])
            for producto in datos:
                escritor.writerow([producto['id'], producto['nombre'], producto['precio'], producto['stock']])
        print(f"Archivo CSV generado en: {ruta_archivo}")


class ExportadorJSON(Exportador):
    def exportar(self, datos, ruta_archivo):
        datos_json = [
            {
                'id': producto['id'],
                'nombre': producto['nombre'],
                'precio': float(producto['precio']),
                'stock': producto['stock'],
            }
            for producto in datos
        ]
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            json.dump(datos_json, file, ensure_ascii=False, indent=4)
        print(f"Archivo JSON generado en: {ruta_archivo}")


class ExportadorPDF(Exportador):
    def exportar(self, datos, ruta_archivo):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')

        pdf.ln(10)

        pdf.set_font("Arial", size=12)

        for producto in datos:
            texto_linea = f"ID: {producto['id']} - Producto: {producto['nombre']} - Precio: ${producto['precio']:.2f} - Stock: {producto['stock']}"
            pdf.cell(200, 10, txt=texto_linea, ln=True)

        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")
