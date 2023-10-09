import pytest
from src.actividad1 import crear_mensaje
@pytest.mark.parametrize(
    "mensaje, nombre",
    [
        ("hola", "cesar")
    ]
)

def test_crear_mensaje_params(nombre, mensaje):
    assert crear_mensaje(nombre) == "hola cesar"