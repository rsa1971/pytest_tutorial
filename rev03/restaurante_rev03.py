class RestauranteTres:
    def __init__(self, nome, pedidos_na_fila=0):
        self.nome = nome
        if pedidos_na_fila >= 0:
            self.pedidos_na_fila = pedidos_na_fila
        else:
            raise ValueError(
                "A quantidade de pedidos na fila deve ser maior ou igual a zero."
            )

    def adiciona_pedido(self):
        self.pedidos_na_fila += 1

    def remove_pedido(self):
        if self.pedidos_na_fila > 0:
            self.pedidos_na_fila -= 1


# Para usar o debug, necessita das linhas abaixo
r = RestauranteTres("X", 5)
print(r.nome)
print(r.pedidos_na_fila)
r.adiciona_pedido()
print(r.pedidos_na_fila)
r.remove_pedido()
print(r.pedidos_na_fila)
