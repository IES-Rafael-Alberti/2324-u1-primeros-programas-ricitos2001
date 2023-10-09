import pytest
from src.plantilla import crear_funcion
@pytest.mark.parametrize(
    "funcion3, funcion",
    [
        ("la funcion es: ","funcion")
    ]  
)
def test_crear_funcion_params(funcion, funcion3):
    assert crear_funcion(funcion) == "la funcion es: funcion"