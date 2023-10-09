import pytest
from src.actividad5 import crear_precio
@pytest.mark.parametrize(
    "preciototal, importe",
    [
        ("precio total: ","importe")
    ]  
)
def test_crear_precio_params(importe, preciototal):
    assert crear_precio(importe) == "precio total: importe€"