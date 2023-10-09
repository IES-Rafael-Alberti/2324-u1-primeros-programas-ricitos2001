import pytest
from src.actividad20 import crear_numerosindigitos
@pytest.mark.parametrize(
    "formatocorrecto, formatoendigitos",
    [
        ("su numero sin digitos es: ", "formatoendigitos")
    ]
)
def test_crear_numerosindigitos_params(formatoendigitos,formatocorrecto):
    assert crear_numerosindigitos(formatoendigitos)=="su numero sin digitos es: formatoendigitos"

