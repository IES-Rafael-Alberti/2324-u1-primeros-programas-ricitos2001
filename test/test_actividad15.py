import pytest
from src.actividad15 import crear_primeraño
from src.actividad15 import crear_segundoaño
from src.actividad15 import crear_terceraño
@pytest.mark.parametrize(
    "dineroprimeraño, primeraño",
    [
        ("primer año: ", "primeraño"),
    ]
)
def test_crear_primeraño_params(primeraño, dineroprimeraño):
    assert crear_primeraño(primeraño) == "primer año: primeraño€"
@pytest.mark.parametrize(
    "dinerosegundoaño, segundoaño",
    [
        ("segundo año: ", "segundoaño"),
    ]
)
def test_crear_segundoaño_params(segundoaño, dinerosegundoaño):
    assert crear_segundoaño(segundoaño) == "segundo año: segundoaño€"
@pytest.mark.parametrize(
    "dineroterceraño, terceraño",
    [
        ("tercer año: ", "terceraño"),
    ]
)
def test_crear_terceraño_params(terceraño, dineroterceraño):
    assert crear_terceraño(terceraño) == "tercer año: terceraño€"
