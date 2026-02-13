# app/tests/test_main.py

import pytest
from app.main import validar_usuario


def test_mayor_de_edad():
    assert validar_usuario("Ana", 25) == "Ana es mayor de edad"


def test_menor_de_edad():
    assert validar_usuario("Juan", 15) == "Juan es menor de edad"


def test_nombre_vacio():
    # Esperamos que falle si el nombre está vacío
    from pytest import raises

    with raises(ValueError):
        validar_usuario("", 20)


def test_edad_negativa():
    from pytest import raises

    with raises(ValueError):
        validar_usuario("Pedro", -1)
