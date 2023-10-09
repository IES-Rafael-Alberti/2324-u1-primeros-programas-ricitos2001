import pytest
from src.actividad13 import crear_cociente
from src.actividad13 import crear_resto
@pytest.mark.parametrize(
    "resultadocociente, cociente",
    [
        ("el cociente es: ", "cociente")
    ]
)
def test_crear_cociente_params(cociente,resultadocociente):
    assert crear_cociente(cociente)=="el cociente es: cociente"
@pytest.mark.parametrize(
    "resultadoresto, resto",
    [
        ("el resto es: ", "resto")
    ]
)
def test_crear_resto_params(resto,resultadoresto):
    assert crear_resto(resto)=="el resto es: resto"