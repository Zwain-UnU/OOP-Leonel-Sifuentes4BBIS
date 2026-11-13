from Controller.database_connection import Database_connection


class PerfilModel:
    def __init__(self):
        self.db = Database_connection()

    def obtener_todos(self):
        query = """
            SELECT id_perfil, username, gemas, racha_dias,
                   notificaciones_activas, meses_suscripcion, es_pro, tipo
            FROM perfiles_moviles
            ORDER BY id_perfil
        """
        return self.db.ejecutar_consulta(query)

    def obtener_por_id(self, id_perfil):
        query = """
            SELECT id_perfil, username, gemas, racha_dias,
                   notificaciones_activas, meses_suscripcion, es_pro, tipo
            FROM perfiles_moviles
            WHERE id_perfil = %s
        """
        filas = self.db.ejecutar_consulta(query, (id_perfil,))
        return filas[0] if filas else None

    def guardar(self, perfil):
        query = """
            INSERT INTO perfiles_moviles
                (username, gemas, racha_dias, notificaciones_activas,
                 meses_suscripcion, es_pro, tipo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            perfil.username,
            perfil.gemas,
            perfil.racha_dias,
            int(perfil.notificaciones_activas),
            getattr(perfil, "meses_suscripcion", 0),
            int(getattr(perfil, "es_pro", False)),
            "Pro" if hasattr(perfil, "meses_suscripcion") else "Movil",
        )
        return self.db.ejecutar_comando(query, params)

    def actualizar(self, id_perfil, perfil):
        query = """
            UPDATE perfiles_moviles
            SET username = %s,
                gemas = %s,
                racha_dias = %s,
                notificaciones_activas = %s,
                meses_suscripcion = %s,
                es_pro = %s,
                tipo = %s
            WHERE id_perfil = %s
        """
        params = (
            perfil.username,
            perfil.gemas,
            perfil.racha_dias,
            int(perfil.notificaciones_activas),
            getattr(perfil, "meses_suscripcion", 0),
            int(getattr(perfil, "es_pro", False)),
            "Pro" if hasattr(perfil, "meses_suscripcion") else "Movil",
            id_perfil,
        )
        return self.db.ejecutar_comando(query, params)

    def eliminar(self, id_perfil):
        query = "DELETE FROM perfiles_moviles WHERE id_perfil = %s"
        return self.db.ejecutar_comando(query, (id_perfil,))
