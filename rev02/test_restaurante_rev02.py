import pytest

from restaurante_rev02 import Restaurante2


def test_pedidos_na_fila_valor_inicial_padrão_igual_a_zero_rev02():
    restaurante2 = Restaurante2("Pizzaria X")
    assert restaurante2.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero_rev02():
    restaurante2 = Restaurante2("Pizzaria X", 1)
    assert restaurante2.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero_rev02():
    with pytest.raises(ValueError):
        Restaurante2("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila_rev02():
    restaurante2 = Restaurante2("Pizzaria X", 1)
    restaurante2.adiciona_pedido()
    assert restaurante2.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila_rev02():
    restaurante2 = Restaurante2("Pizzaria X", 1)
    restaurante2.remove_pedido()
    assert restaurante2.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia_rev02():
    restaurante2 = Restaurante2("Pizzaria X")
    restaurante2.remove_pedido()
    assert restaurante2.pedidos_na_fila == 0
