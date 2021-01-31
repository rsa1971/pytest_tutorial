import pytest

from restaurante_rev02 import RestauranteDois


@pytest.fixture
def RestauranteDois_fila_vazia():
    return RestauranteDois("Pizzaria X")


@pytest.fixture
def RestauranteDois_com_um_pedido():
    return RestauranteDois("Pizzaria X", 1)


def test_pedidos_na_fila_valor_inicial_padrão_igual_a_zero_rev02(RestauranteDois_fila_vazia):
    assert RestauranteDois_fila_vazia.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero_rev02(RestauranteDois_com_um_pedido):
    assert RestauranteDois_com_um_pedido.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero_rev02():
    with pytest.raises(ValueError):
        RestauranteDois("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila_rev02(RestauranteDois_com_um_pedido):
    RestauranteDois_com_um_pedido.adiciona_pedido()
    assert RestauranteDois_com_um_pedido.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila_rev02(RestauranteDois_com_um_pedido):
    RestauranteDois_com_um_pedido.remove_pedido()
    assert RestauranteDois_com_um_pedido.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia_rev02(RestauranteDois_fila_vazia):
    RestauranteDois_fila_vazia.remove_pedido()
    assert RestauranteDois_fila_vazia.pedidos_na_fila == 0


@pytest.mark.parametrize("inicial, final", [(0, 0), (1, 0), (2, 1)])
def test_remocao_de_pedidos(inicial, final):
    restauranteDois = RestauranteDois("Pizzaria X", inicial)
    restauranteDois.remove_pedido()
    assert restauranteDois.pedidos_na_fila == final
