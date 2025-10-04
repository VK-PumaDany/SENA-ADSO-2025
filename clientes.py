class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.historial_pedidos = []

    def realizar_pedido(self, pedido):
        if pedido.cantidad_platos() == 0:
            print(
                f"No se puede realizar el pedido porque no tiene ningún plato almacenado \n"
            )
        else:
            self.historial_pedidos.append(pedido)
            print(f"Pedido agregado con exito \n")

    def listar_pedidos(self):
        for pedidos in self.historial_pedidos:
            pedidos.mostrar_detalle_pedido()

    def detalle_cliente(self):
        print(f"Nombre: {self.nombre}")
        print(f"Telefono {self.telefono}")
        print(f"Numero de pedidos {len(self.historial_pedidos)}")


# Clientes

Angelo = Cliente("Angelo", "3211111111")
Alexa = Cliente("Alexa", "3218432903")
Karol = Cliente("Karol", "3215234823")
Sebas = Cliente("Sebas", "3194237834")
