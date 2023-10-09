import pytest
from src.actividad26 import crear_lista
@pytest.mark.parametrize(
    "resultadolista",
    [
        ("resultadolista")
    ]  
)
def test_crear_lista_params(resultadolista):
    assert crear_lista(resultadolista) == "resultadolista"
