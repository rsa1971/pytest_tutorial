import pytest

from restaurante_rev03 import RestauranteTres


def test_pedidos_na_fila_valor_inicial_padrão_igual_a_zero_rev03():
    restaurante3 = RestauranteTres("Pizzaria X")
    assert restaurante3.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero_rev03():
    restaurante3 = RestauranteTres("Pizzaria X", 1)
    assert restaurante3.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero_rev03():
    with pytest.raises(ValueError):
        RestauranteTres("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila_rev03():
    restaurante3 = RestauranteTres("Pizzaria X", 1)
    restaurante3.adiciona_pedido()
    assert restaurante3.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila_rev03():
    restaurante3 = RestauranteTres("Pizzaria X", 1)
    restaurante3.remove_pedido()
    assert restaurante3.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia_rev03():
    restaurante3 = RestauranteTres("Pizzaria X")
    restaurante3.remove_pedido()
    assert restaurante3.pedidos_na_fila == 0
