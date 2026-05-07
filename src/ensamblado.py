# =========================
# Componente
# =========================

class Componente:

    def mostrar(self, nivel=0):
        pass


# =========================
# Leaf
# =========================

class Pieza(Componente):

    def __init__(self, nombre):
        self.nombre = nombre


    def mostrar(self, nivel=0):

        print(" " * nivel + f"Pieza: {self.nombre}")


# =========================
# Composite
# =========================

class SubConjunto(Componente):

    def __init__(self, nombre):

        self.nombre = nombre
        self.componentes = []


    def agregar(self, componente):

        self.componentes.append(componente)


    def mostrar(self, nivel=0):

        print(" " * nivel + f"Subconjunto: {self.nombre}")

        for componente in self.componentes:
            componente.mostrar(nivel + 4)


# =========================
# Producto Principal
# =========================

producto = SubConjunto("Producto Principal")


# =========================
# Crear 3 subconjuntos
# =========================

for i in range(1, 4):

    subconjunto = SubConjunto(f"Subconjunto {i}")

    # Agregar 4 piezas a cada subconjunto
    for j in range(1, 5):

        pieza = Pieza(f"Pieza {i}.{j}")
        subconjunto.agregar(pieza)

    producto.agregar(subconjunto)


# =========================
# Subconjunto opcional
# =========================

opcional = SubConjunto("Subconjunto Opcional")

for i in range(1, 5):

    pieza = Pieza(f"Pieza Opcional {i}")
    opcional.agregar(pieza)

producto.agregar(opcional)


# =========================
# Mostrar estructura
# =========================

producto.mostrar()