import pytest
from src.actividad22 import crear_mayuscula
@pytest.mark.parametrize(
    "resultado, fraseconvocalmayuscula",
    [
        ("resultado", "fraseconvocalmayuscula")
    ]
)

def test_crear_mayuscula_params(fraseconvocalmayuscula, resultado):
    assert crear_mayuscula(fraseconvocalmayuscula) == "fraseconvocalmayuscula"