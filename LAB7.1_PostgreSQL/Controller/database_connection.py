import psycopg2
from psycopg2.extras import RealDictCursor
from .config import DB_CONFIG

class Database_connection:
    def __init__(self):
        self.config = DB_CONFIG

    def get_connection(self):
        try:
            conexion = psycopg2.connect(**self.config)
            return conexion
        except Exception as e:
            print(f"Error al conectar con PostgreSQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.get_connection()
        if not conexion:
            return None

        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()