import pytest
from src.actividad16 import crear_precio
from src.actividad16 import crear_descuento
from src.actividad16 import crear_costetotal
@pytest.mark.parametrize(
    "preciopan, precio",
    [
        ("precio del pan: ", "precio"),
    ]
)
def test_crear_precio_params(precio, preciopan):
    assert crear_precio(precio) == "precio del pan: precio€"
@pytest.mark.parametrize(
    "descuentopan, descuento",
    [
        ("descuento de las barras tiesas: ", "descuento"),
    ]
)
def test_crear_descuento_params(descuento, descuentopan):
    assert crear_descuento(descuento) == "descuento de las barras tiesas: descuento€"
@pytest.mark.parametrize(
    "costepan, costetotal",
    [
        ("coste total de las barras tiesas: ", "costetotal"),
    ]
)
def test_crear_costetotal_params(costetotal, costepan):
    assert crear_costetotal(costetotal) == "coste total de las barras tiesas: costetotal€"
