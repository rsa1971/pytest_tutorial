import pytest

from restaurante import Restaurante


def test_pedidos_na_fila_valor_inicial_padrão_igual_a_zero():
    restaurante = Restaurante("Pizzaria X")
    assert restaurante.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero():
    restaurante = Restaurante("Pizzaria X", 1)
    assert restaurante.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurante("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila():
    restaurante = Restaurante("Pizzaria X", 1)
    restaurante.adiciona_pedido()
    assert restaurante.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila():
    restaurante = Restaurante("Pizzaria X", 1)
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia():
    restaurante = Restaurante("Pizzaria X")
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == 0
