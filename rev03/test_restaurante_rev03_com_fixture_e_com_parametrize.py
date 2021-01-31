import pytest

from restaurante_rev03 import RestauranteTres


@pytest.fixture
def restaurante3_fila_vazia():
    return RestauranteTres("Pizzaria X")


@pytest.fixture
def restaurante3_com_um_pedido():
    return RestauranteTres("Pizzaria X", 1)


def test_pedidos_na_fila_valor_inicial_padrão_igual_a_zero_rev03(restaurante3_fila_vazia):
    assert restaurante3_fila_vazia.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero_rev03(restaurante3_com_um_pedido):
    assert restaurante3_com_um_pedido.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero_rev03():
    with pytest.raises(ValueError):
        RestauranteTres("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila_rev03(restaurante3_com_um_pedido):
    restaurante3_com_um_pedido.adiciona_pedido()
    assert restaurante3_com_um_pedido.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila_rev03(restaurante3_com_um_pedido):
    restaurante3_com_um_pedido.remove_pedido()
    assert restaurante3_com_um_pedido.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia_rev03(restaurante3_fila_vazia):
    restaurante3_fila_vazia.remove_pedido()
    assert restaurante3_fila_vazia.pedidos_na_fila == 0


@pytest.mark.parametrize("inicial, final", [(0, 0), (1, 0), (2, 1)])
def test_remocao_de_pedidos(inicial, final):
    restaurante3 = RestauranteTres("Pizzaria", inicial)
    restaurante3.remove_pedido()
    assert restaurante3.pedidos_na_fila == final
