class Pedidio:
    def __init__(self, id):
        self.id = id
        self.platos = []
        self.total = 0

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def calcular_total(self, mostrar_total=True):
        for plato in self.platos:
            self.total += plato.precio
        if mostrar_total:
            self.mostrar_total()

    def mostrar_total(self):
        print(f"El precio total del pedido es {self.total}")

    def cantidad_platos(self):
        print(f"El total de platos es {len(self.platos)}")
        return len(self.platos)

    def mostrar_detalle_pedido(self):
        print(f"Código {self.id} \n")
        for plato in self.platos:
            plato.ver_informacion()
        print(f"Total del pedido {self.calcular_total()}")


# Pedidos

# Pedido de Angelo
