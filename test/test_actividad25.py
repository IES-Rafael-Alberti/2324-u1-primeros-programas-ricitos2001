import pytest
from src.actividad25 import crear_fecha
@pytest.mark.parametrize(
    "fecha, fechacimiento",
    [
        ("fecha de nacimiento: ", "fechanacimiento"),
    ]
)
def test_crear_fecha_params(fechacimiento, fecha):
    assert crear_fecha(fechacimiento) == "fecha de nacimiento: fechanacimiento"

