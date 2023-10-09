import pytest
from src.actividad9 import crear_resultado
@pytest.mark.parametrize(
    "resultado",
    [
        ("el resultado es: ")
    ]  
)
def test_crear_resultado_params(resultado):
    assert crear_resultado(resultado) == "el resultado es: "