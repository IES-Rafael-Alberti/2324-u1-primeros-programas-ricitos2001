import pytest
from src.actividad4 import crear_farenheit
@pytest.mark.parametrize(
    "resultado, farenheit",
    [
        ("grados farenheit: ", "farenheit")
    ]
)
def test_crear_farenheit_params(farenheit, resultado):
    assert crear_farenheit(farenheit) == "grados farenheit: farenheitFº"