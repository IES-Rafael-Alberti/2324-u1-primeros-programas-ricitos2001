import pytest
from src.actividad3 import crear_total
@pytest.mark.parametrize(
    "sumatotal, total",
    [
        ("total: ", "sumatotal")
    ]
)
def test_crear_total_params(total, sumatotal):
    assert crear_total(total) == "total: sumatotal"