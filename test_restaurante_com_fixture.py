import pytest

from restaurante import Restaurante

@pytest.fixture()
def restaurante_fila_vazia():
    return Restaurante("Pizzaria X")


@pytest.fixture()
def restaurante_com_um_pedido():
    return Restaurante("Pizzaria X", 1)


def test_pedidos_na_fila_valor_inicial_padrão_igual_a_zero(restaurante_fila_vazia):
    assert restaurante_fila_vazia.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero(restaurante_com_um_pedido):
    assert restaurante_com_um_pedido.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurante("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila(restaurante_com_um_pedido):
    restaurante_com_um_pedido.adiciona_pedido()
    assert restaurante_com_um_pedido.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila(restaurante_com_um_pedido):
    restaurante_com_um_pedido.remove_pedido()
    assert restaurante_com_um_pedido.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia(restaurante_fila_vazia):
    restaurante_fila_vazia.remove_pedido()
    assert restaurante_fila_vazia.pedidos_na_fila == 0