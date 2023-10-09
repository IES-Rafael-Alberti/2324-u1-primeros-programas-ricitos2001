import pytest
from src.actividad8 import crear_resultado
@pytest.mark.parametrize(
    "suma, resultado",
    [
        ("el resultado es: ","suma")
    ]  
)
def test_crear_resultado_params(resultado, suma):
    assert crear_resultado(resultado) == "el resultado es: suma"