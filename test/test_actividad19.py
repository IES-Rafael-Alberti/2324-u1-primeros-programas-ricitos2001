import pytest
from src.actividad19 import crear_mayusculas
from src.actividad19 import crear_total
@pytest.mark.parametrize(
    "nombremayusculas, letrasmayusculas",
    [
        ("nombre en mayusculas: ", "letrasmayusculas")
    ]
)
def test_crear_mayusculas_params(letrasmayusculas,nombremayusculas):
    assert crear_mayusculas(letrasmayusculas)=="nombre en mayusculas: letrasmayusculas"
@pytest.mark.parametrize(
    "totalletras, numeroletras",
    [
        ("numero de letras: ", "numeroletras")
    ]
)
def test_crear_total_params(numeroletras,totalletras):
    assert crear_total(numeroletras)=="numero de letras: numeroletras"