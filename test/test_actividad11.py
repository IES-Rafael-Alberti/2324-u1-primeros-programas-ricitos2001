import pytest
from src.actividad10 import crear_calculo
@pytest.mark.parametrize(
    "resultado, calculo",
    [
        ("el resultado es: ","calculo")
    ]  
)
def test_crear_calculo_params(calculo, resultado):
    assert crear_calculo(calculo) == "el resultado es: calculo"