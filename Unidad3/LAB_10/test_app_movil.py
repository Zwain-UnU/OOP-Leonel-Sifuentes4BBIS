import pytest

from app_movil import (
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)


@pytest.fixture
def perfil():
    return PerfilMovil("leonel")


@pytest.fixture
def perfil_pro():
    return PerfilPro("leonel_pro", meses_suscripcion=3)


def test_valores_iniciales_del_perfil(perfil):
    assert perfil.username == "leonel"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_gemas_negativas_en_construccion():
    with pytest.raises(ValueError):
        PerfilMovil("invalido", gemas=-1)


def test_ganar_gemas_incrementa_el_saldo(perfil):
    assert perfil.ganar_gemas(10) == 60
    assert perfil.gemas == 60


@pytest.mark.parametrize(
    "cantidad, saldo_esperado",
    [(1, 51), (10, 60), (50, 100), (100, 150)],
)
def test_ganar_gemas_parametrizado(perfil, cantidad, saldo_esperado):
    assert perfil.ganar_gemas(cantidad) == saldo_esperado


@pytest.mark.parametrize("cantidad", [0, -1, -50])
def test_ganar_gemas_rechaza_cantidades_no_positivas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


def test_gastar_gemas_decrementa_el_saldo(perfil):
    assert perfil.gastar_gemas(20) == 30
    assert perfil.gemas == 30


def test_gastar_gemas_insuficientes_lanza_excepcion(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(51)


@pytest.mark.parametrize("cantidad", [0, -10])
def test_gastar_gemas_rechaza_cantidades_no_positivas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)


def test_perfil_pro_hereda_de_perfil_movil(perfil_pro):
    assert isinstance(perfil_pro, PerfilMovil)
    assert isinstance(perfil_pro, PerfilPro)


def test_valores_iniciales_del_perfil_pro(perfil_pro):
    assert perfil_pro.es_pro is True
    assert perfil_pro.meses_suscripcion == 3
    assert perfil_pro.gemas == 50


@pytest.mark.parametrize("meses", [0, -1, -12])
def test_perfil_pro_rechaza_periodo_inicial_invalido(meses):
    with pytest.raises(ValueError):
        PerfilPro("invalido", meses_suscripcion=meses)


def test_perfil_pro_hereda_operaciones_de_gemas(perfil_pro):
    assert perfil_pro.ganar_gemas(25) == 75
    assert perfil_pro.gastar_gemas(5) == 70


def test_descargar_contenido_offline_exitoso(perfil_pro):
    resultado = perfil_pro.descargar_contenido_offline()

    assert "habilitada" in resultado
    assert perfil_pro.es_pro is True


def test_descargar_contenido_con_suscripcion_expirada(perfil_pro):
    perfil_pro.meses_suscripcion = 0

    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()

    assert perfil_pro.es_pro is False
