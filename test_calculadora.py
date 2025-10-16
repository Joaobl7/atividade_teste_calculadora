# test_calculadora.py
import pytest
from calculadora import Calculadora

c = Calculadora()

def test_soma():
    assert c.soma(3, 2) == 5

def test_subtracao():
    assert c.subtracao(10, 4) == 6

def test_multiplicacao():
    assert c.multiplicacao(2, 3) == 6

def test_divisao():
    assert c.divisao(9, 3) == 3

def test_divisao_zero():
    with pytest.raises(ValueError):
        c.divisao(5, 0)

def test_potenciacao():
    assert c.potenciacao(2, 4) == 16

def test_raiz_quadrada():
    assert c.raiz_quadrada(25) == 5

def test_raiz_negativa():
    with pytest.raises(ValueError):
        c.raiz_quadrada(-1)

def test_media():
    assert c.media([2, 4, 6]) == 4

def test_media_vazia():
    with pytest.raises(ValueError):
        c.media([])

def test_modulo():
    assert c.modulo(-8) == 8

def test_percentual():
    assert c.percentual(30, 120) == 25

def test_percentual_total_zero():
    with pytest.raises(ValueError):
        c.percentual(10, 0)
