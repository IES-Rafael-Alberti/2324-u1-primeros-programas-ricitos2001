import pytest
from src.actividad18 import crear_minusculas
from src.actividad18 import crear_mayusculas
from src.actividad18 import crear_capitalizado
@pytest.mark.parametrize(
    "nombreminusculas, letrasminusculas",
    [
        ("nombre en minusculas: ", "letrasminusculas"),
    ]
)
def test_crear_minusculas_params(letrasminusculas, nombreminusculas):
    assert crear_minusculas(letrasminusculas) == "nombre en minusculas: letrasminusculas"
@pytest.mark.parametrize(
    "nombremayusculas, letrasmayusculas",
    [
        ("nombre en mayusculas: ", "letrasmayusculas"),
    ]
)
def test_crear_mayusculas_params(letrasmayusculas, nombremayusculas):
    assert crear_mayusculas(letrasmayusculas) == "nombre en mayusculas: letrasmayusculas"
@pytest.mark.parametrize(
    "nombrecapitalizado, letrascapitalizadas",
    [
        ("nombre capitalizado: ", "letrascapitalizadas"),
    ]
)
def test_crear_capitalizado_params(letrascapitalizadas, nombrecapitalizado):
    assert crear_capitalizado(letrascapitalizadas) == "nombre capitalizado: letrascapitalizadas"
