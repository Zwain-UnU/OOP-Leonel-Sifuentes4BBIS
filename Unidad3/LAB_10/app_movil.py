class SuscripcionExpiradaError(Exception):
    """Se lanza al intentar una operación restringida sin suscripción activa."""


class PuntosInsuficientesError(Exception):
    """Se lanza cuando una transacción supera el saldo de gemas disponible."""


class PerfilMovil:
    def __init__(self, username, gemas=50, racha_dias=1, notificaciones_activas=True):
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    @property
    def gemas(self):
        return self._gemas

    @gemas.setter
    def gemas(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("Las gemas deben ser un número entero.")
        if valor < 0:
            raise ValueError("El saldo de gemas no puede ser negativo.")
        self._gemas = valor

    def ganar_gemas(self, cantidad: int) -> int:
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad a ganar debe ser estrictamente positiva.")

        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad a gastar debe ser estrictamente positiva.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError(
                f"Gemas insuficientes: intentas gastar {cantidad} y tienes {self.gemas}."
            )

        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(
        self,
        username,
        meses_suscripcion,
        gemas=50,
        racha_dias=1,
        notificaciones_activas=True,
    ):
        if isinstance(meses_suscripcion, bool) or not isinstance(meses_suscripcion, int):
            raise ValueError("Los meses de suscripción deben ser un número entero.")
        if meses_suscripcion <= 0:
            raise ValueError("El periodo inicial de suscripción debe ser mayor que cero.")

        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    @classmethod
    def desde_bd(
        cls,
        username,
        meses_suscripcion,
        gemas=50,
        racha_dias=1,
        notificaciones_activas=True,
        es_pro=True,
    ):
        perfil = cls(
            username,
            meses_suscripcion if meses_suscripcion > 0 else 1,
            gemas,
            racha_dias,
            notificaciones_activas,
        )
        perfil.meses_suscripcion = meses_suscripcion
        perfil.es_pro = es_pro
        return perfil

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError(
                "La suscripción ha expirado. Renueva tu plan para descargar contenido offline."
            )

        return f"Descarga offline habilitada para {self.username}."
