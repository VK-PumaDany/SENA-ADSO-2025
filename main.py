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
        self.menu.append(plato)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def generar_reporte(self):
        print("REPORTE")
        self.reportes_generados += 1
        for cliente in self.clientes:
            cliente.detalle_cliente()
            print("\n")


# Restaurante

la_nota = Restaurante("La Nota")


# Registro de platos

la_nota.registrar_plato(extra_chesse_hamburger)
la_nota.registrar_plato(big_hamburger)
la_nota.registrar_plato(hot_dog)
la_nota.registrar_plato(hot_dog)
la_nota.registrar_plato(beer)
la_nota.registrar_plato(cocacola)
la_nota.registrar_plato(tea)

# Registro de clientes

la_nota.registrar_cliente(Angelo)
la_nota.registrar_cliente(Alexa)
la_nota.registrar_cliente(Karol)
la_nota.registrar_cliente(Sebas)

la_nota.generar_reporte()
