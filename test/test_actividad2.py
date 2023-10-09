import pytest
from src.actividad2 import crear_importe
@pytest.mark.parametrize(
    "importetotal, importe",
    [
        ("importe total: ", "importe")
    ]
)
def test_crear_importe_params(importe, importetotal):
    assert crear_importe(importe) == "importe total: importe€"