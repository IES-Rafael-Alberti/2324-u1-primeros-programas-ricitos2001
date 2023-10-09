import pytest
from src.actividad17 import crear_repeticiones
@pytest.mark.parametrize(
    "texto",
    [
        ("texto")
    ]  
)
def test_crear_repeticiones_params(texto):
    assert crear_repeticiones(texto) == "texto"