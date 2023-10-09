import pytest
from src.actividad27 import crear_mensaje
@pytest.mark.parametrize(
    "nombre,precio,unidad,preciounidad",
    [
        ("nombre","precio","unidad","preciounidad")
    ]
)

def test_crear_mensaje_params(nombre,precio,unidad,preciounidad):
    assert crear_mensaje(nombre,precio,unidad,preciounidad) == "nombre, precio€, unidad, preciounidad€"