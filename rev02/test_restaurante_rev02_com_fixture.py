import pytest

from restaurante_rev02 import Restaurante2


@pytest.fixture
def restaurante2_fila_vazia():
    return Restaurante2("Pizzaria X")


@pytest.fixture
def restaurante2_com_um_pedido():
    return Restaurante2("Pizzaria X", 1)


def test_pedidos_na_fila_valor_inicial_padrão_igual_a_zero_rev02(restaurante2_fila_vazia):
    assert restaurante2_fila_vazia.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero_rev02(restaurante2_com_um_pedido):
    assert restaurante2_com_um_pedido.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero_rev02():
    with pytest.raises(ValueError):
        Restaurante2("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila_rev02(restaurante2_com_um_pedido):
    restaurante2_com_um_pedido.adiciona_pedido()
    assert restaurante2_com_um_pedido.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila_rev02(restaurante2_com_um_pedido):
    restaurante2_com_um_pedido.remove_pedido()
    assert restaurante2_com_um_pedido.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia_rev02(restaurante2_fila_vazia):
    restaurante2_fila_vazia.remove_pedido()
    assert restaurante2_fila_vazia.pedidos_na_fila == 0
