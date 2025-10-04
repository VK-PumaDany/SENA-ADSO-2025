class Plato:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def ver_informacion(self):
        print(f"Nombre del plato {self.nombre} \n")
        print(f"Categoria {self.categoria} \n")
        print(f"Precio {self.precio}")


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
