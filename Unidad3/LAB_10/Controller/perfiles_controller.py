from Models.perfil_model import PerfilModel
from app_movil import (
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)


class PerfilController:
    def __init__(self):
        self.modelo = PerfilModel()

    def listar(self):
        return self.modelo.obtener_todos() or []

    def crear(self, username, es_pro=False, meses_suscripcion=0):
        username = username.strip()

        if not username:
            return False, "El nombre de usuario es obligatorio."

        try:
            if es_pro:
                perfil = PerfilPro(username, meses_suscripcion)
            else:
                perfil = PerfilMovil(username)
        except ValueError as error:
            return False, str(error)

        if not self.modelo.guardar(perfil):
            return False, "No se pudo guardar el perfil en MySQL."

        return True, f"Perfil '{username}' creado correctamente."

    def _recuperar_perfil(self, id_perfil):
        fila = self.modelo.obtener_por_id(id_perfil)

        if not fila:
            return None, "Perfil no encontrado."

        if fila["tipo"] == "Pro":
            perfil = PerfilPro.desde_bd(
                username=fila["username"],
                meses_suscripcion=fila["meses_suscripcion"],
                gemas=fila["gemas"],
                racha_dias=fila["racha_dias"],
                notificaciones_activas=bool(fila["notificaciones_activas"]),
                es_pro=bool(fila["es_pro"]),
            )
        else:
            perfil = PerfilMovil(
                username=fila["username"],
                gemas=fila["gemas"],
                racha_dias=fila["racha_dias"],
                notificaciones_activas=bool(fila["notificaciones_activas"]),
            )

        return perfil, None

    def ganar_gemas(self, id_perfil, cantidad=10):
        perfil, error = self._recuperar_perfil(id_perfil)

        if error:
            return False, error

        try:
            perfil.ganar_gemas(cantidad)
        except ValueError as error:
            return False, str(error)

        if not self.modelo.actualizar(id_perfil, perfil):
            return False, "No se pudo actualizar el perfil en MySQL."

        return True, f"{perfil.username} ahora tiene {perfil.gemas} gemas."

    def gastar_gemas(self, id_perfil, cantidad=10):
        perfil, error = self._recuperar_perfil(id_perfil)

        if error:
            return False, error

        try:
            perfil.gastar_gemas(cantidad)
        except (ValueError, PuntosInsuficientesError) as error:
            return False, str(error)

        if not self.modelo.actualizar(id_perfil, perfil):
            return False, "No se pudo actualizar el perfil en MySQL."

        return True, f"{perfil.username} ahora tiene {perfil.gemas} gemas."

    def descargar_offline(self, id_perfil):
        perfil, error = self._recuperar_perfil(id_perfil)

        if error:
            return False, error

        if not hasattr(perfil, "descargar_contenido_offline"):
            return False, "Solo los perfiles Pro pueden descargar contenido offline."

        try:
            mensaje = perfil.descargar_contenido_offline()
        except SuscripcionExpiradaError as error:
            self.modelo.actualizar(id_perfil, perfil)
            return False, str(error)

        if not self.modelo.actualizar(id_perfil, perfil):
            return False, "No se pudo actualizar el perfil en MySQL."

        return True, mensaje

    def eliminar(self, id_perfil):
        if not self.modelo.eliminar(id_perfil):
            return False, "No se pudo eliminar el perfil."

        return True, "Perfil eliminado correctamente."
