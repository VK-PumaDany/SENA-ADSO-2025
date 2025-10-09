from plato import *
from clientes import *
from pedido import *


class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []
        self.clientes = []
        self.reportes_generados = 0

    def registrar_plato(self, plato):
        if plato.is_registred:
            print(f"El plato {plato.nombre} ya esya registrado")
        else:
            plato.is_registred = True
            self.menu.append(plato)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def generar_reporte(self):
        print("REPORTE")
        self.reportes_generados += 1
        for cliente in self.clientes:
            cliente.detalle_cliente()
            print("\n")

        mostrar_menu = input("Desea ver el menu del restaurante (si): ")

        if mostrar_menu == "si":
            self.ver_menu_platos()

    def ver_menu_platos(self):
        if len(self.menu) == 0:
            print("No hay ningun plato registrado")
        else:
            print("MENÚ")
            for plato in self.menu:
                print(f"{plato.nombre} {plato.precio} {plato.is_registred}")


# Restaurante

la_nota = Restaurante("La Nota")


# Registro de platos

la_nota.registrar_plato(extra_chesse_hamburger)
la_nota.registrar_plato(big_hamburger)
la_nota.registrar_plato(hot_dog)
la_nota.registrar_plato(beer)
la_nota.registrar_plato(cocacola)
la_nota.registrar_plato(tea)

# Registro de clientes

la_nota.registrar_cliente(Angelo)
la_nota.registrar_cliente(Alexa)
la_nota.registrar_cliente(Karol)
la_nota.registrar_cliente(Sebas)

# Registro de pedidos

# Pedido angelo

pedido_angelo = Pedido("angelo")
pedido_angelo.agregar_plato(cocacola)
pedido_angelo.agregar_plato(hot_dog)

pedido_angelo.mostrar_detalle_pedido()

Angelo.realizar_pedido(pedido_angelo)

la_nota.generar_reporte()
