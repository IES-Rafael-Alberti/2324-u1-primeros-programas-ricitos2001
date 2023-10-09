import pytest
from src.actividad12 import crear_masa
@pytest.mark.parametrize(
    "resultadomasa, masa",
    [
        ("tu índice de masa corporal es: ", "masa"),
    ]
)
def test_crear_masa_params(masa, resultadomasa):
    assert crear_masa(masa) == "tu índice de masa corporal es: masakg/m2"