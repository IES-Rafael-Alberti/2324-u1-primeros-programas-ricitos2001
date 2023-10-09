import pytest
from src.actividad14 import crear_payasos
from src.actividad14 import crear_muñecas
@pytest.mark.parametrize(
    "totalpayasos, pesototalpayasos",
    [
        ("el peso total del ultimo paquete de payasos es de ", "pesototalpayasos")
    ]
)
def test_crear_payasos_params(pesototalpayasos,totalpayasos):
    assert crear_payasos(pesototalpayasos)=="el peso total del ultimo paquete de payasos es de pesototalpayasosg"
@pytest.mark.parametrize(
    "totalmuñecas, pesototalmuñecas",
    [
        ("el peso total del ultimo paquete de muñecas es de ", "pesototalmuñecas")
    ]
)
def test_crear_muñecas_params(pesototalmuñecas,totalmuñecas):
    assert crear_muñecas(pesototalmuñecas)=="el peso total del ultimo paquete de muñecas es de pesototalmuñecasg"