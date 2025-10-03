class Plato:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def ver_informacion(self):
        print(f"Nombre del plato {self.nombre} \n")
        print(f"Categoria {self.categoria} \n")
        print(f"Precio {self.precio}")


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


class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.historial_pedidos = []
        
    def realizar_pedido(self, pedido):
        if pedido.cantidad_platos() == 0:
            print(f"No se puede realizar el pedido porque no tiene ningún plato almacenado \n")
        else:
            self.historial_pedidos.append(pedido)
            print(f"Pedido agregado con exito \n")
            
        
    def listar_pedidos(self):
        for pedidos in self.historial_pedidos:
            pedidos.mostrar_detalle_pedido()
    
    def detalle_cliente(self):
        print(f"Nombre: {self.nombre} \n")
        print(f"Telefono {self.telefono} \n")
        print(f"Numero de pedidos {len(self.historial_pedidos)}")
        

    
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
            
            
# Restaurante

la_nota = Restaurante("La Nota")

# Platos

# Hamburguesas

big_hamburger = Plato("Hamburgesa Grande", "Comida Rapida", 17500)
extra_chesse_hamburger = Plato("Hamburguesa extra queso", "Comida Rapida", 20000)

# Perros

hot_dog = Plato("Perro caliente", "Comida Rapida", 12000)
hot_dog_dobble = Plato("Perro caliente con doble salchicha", "Comida Rapida", 17000)

# Bebidas

beer = Plato("Cerveza", "Bebida", 4000)
tea = Plato("Tea", "Bebida", 3500)
cocacola = Plato("Cocacola", "Bebida", 4500)

# Clientes

Angelo = Cliente("Angelo", "3211111111")
Alexa = Cliente("Alexa", "3218432903")
Karol = Cliente("Karol", "3215234823")