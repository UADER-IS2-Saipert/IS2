## Singleton
# 1. Factorial

class FactorialSingleton:
    __instance = None  # Variable privada que guarda la única instancia

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance  # Siempre devuelve la misma instancia

    def calcular(self, n):
        # Calcular el factorial de un número
        if n < 0:
            raise ValueError("No existe factorial de números negativos")
        if n == 0 or n == 1:
            return 1
        return n * self.calcular(n - 1)  # Recursividad

f1 = FactorialSingleton()
f2 = FactorialSingleton()

#Ejemplo
print(f1.calcular(5)) 
print(f1 is f2) 
print("=================================================") 

#----------------------------------------------------------------------------------------------------
# 2. Calculadora de impuestos

class CalculadoraImpuestos:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def calcular(self, base):
        # Calcula impuestos sobre la base imponible
        iva = base * 0.21            
        iibb = base * 0.05           
        contribuciones = base * 0.012  

        total = iva + iibb + contribuciones
        return total

#Ejemplo
calc = CalculadoraImpuestos()
print(calc.calcular(1000))
print("=================================================") 

#-----------------------------------------------------------------------------------------------------
##Factory
# 3. Hamburguesa

class Hamburguesa:
    def entregar(self):
        pass


class Mostrador(Hamburguesa):
    def entregar(self):
        print("Entrega en mostrador")


class Retiro(Hamburguesa):
    def entregar(self):
        print("Retiro por el cliente")


class Delivery(Hamburguesa):
    def entregar(self):
        print("Envío por delivery")


class HamburguesaFactory:
    @staticmethod
    def crear(tipo):
        # Selecciona el tipo de entrega al cliente
        if tipo == "mostrador":
            return Mostrador()
        elif tipo == "retiro":
            return Retiro()
        elif tipo == "delivery":
            return Delivery()
        else:
            raise ValueError("Tipo inválido")

# Ejemplo
h = HamburguesaFactory.crear("delivery")
h.entregar()
print("=================================================") 

#----------------------------------------------------------------------------------------------------
# 4. Factura
class Factura:
    def __init__(self, importe):
        self.importe = importe  # Total de la factura

    def mostrar(self):
        pass


class ResponsableInscripto(Factura):
    def mostrar(self):
        print(f"Factura A - IVA Responsable: ${self.importe}")


class NoInscripto(Factura):
    def mostrar(self):
        print(f"Factura B - IVA No Inscripto: ${self.importe}")


class Exento(Factura):
    def mostrar(self):
        print(f"Factura C - IVA Exento: ${self.importe}")


class FacturaFactory:
    @staticmethod
    def crear(tipo, importe):
        # Devuelve el tipo de factura según la condición del cliente
        if tipo == "responsable":
            return ResponsableInscripto(importe)
        elif tipo == "no_inscripto":
            return NoInscripto(importe)
        elif tipo == "exento":
            return Exento(importe)
        else:
            raise ValueError("Tipo inválido")


# Ejemplo
factura = FacturaFactory.crear("responsable", 5000)
factura.mostrar()
print("=================================================") 

#----------------------------------------------------------------------------------------------------
## Builder
# 5. Avión

class Avion:
    def __init__(self):
        self.partes = []  # Lista de partes del avión

    def agregar(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Avión construido con:", ", ".join(self.partes))


class BuilderAvion:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.agregar("Body")

    def construir_turbinas(self):
        self.avion.agregar("2 turbinas")

    def construir_alas(self):
        self.avion.agregar("2 alas")

    def construir_tren(self):
        self.avion.agregar("Tren de aterrizaje")

    def obtener_avion(self):
        return self.avion


# Director controla el orden de construcción
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren()
        return self.builder.obtener_avion()


# Ejemplo
builder = BuilderAvion()
director = Director(builder)

avion = director.construir()
avion.mostrar()
print("=================================================") 

#-------------------------------------------------------------------------------------------------
## Prototype
# Clonacion
class Prototipo:
    def clonar(self):
        # Método que será sobrescrito por las clases hijas
        pass

class Ejemplo(Prototipo):
    def __init__(self, valor):
        self.valor = valor

    def clonar(self):
        # Creamos una nueva instancia con el mismo valor
        return Ejemplo(self.valor)

obj1 = Ejemplo(10)

# Clonamos
obj2 = obj1.clonar()
obj3 = obj2.clonar()

# Mostramos valores
print(obj1.valor, obj2.valor, obj3.valor)

# Verificamos que son objetos distintos
print(obj1 is obj2) 
print(obj2 is obj3)
print("=================================================") 

#----------------------------------------------------------------------------------------------------
## Abstract
# 7. River y Boca

class Jugador:
    def jugar(self):
        pass  


class Tecnico:
    def dirigir(self):
        pass


class EstiloJuego:
    def estrategia(self):
        pass

#River
class JugadorRiver(Jugador):
    def jugar(self):
        print("Jugador de River juega con posesión y ataque")


class TecnicoRiver(Tecnico):
    def dirigir(self):
        print("Técnico de River usa presión alta y juego ofensivo")


class EstiloRiver(EstiloJuego):
    def estrategia(self):
        print("Estilo River: ofensivo, posesión y presión constante")

#Boca
class JugadorBoca(Jugador):
    def jugar(self):
        print("Jugador de Boca juega fuerte y defensivo")


class TecnicoBoca(Tecnico):
    def dirigir(self):
        print("Técnico de Boca prioriza orden defensivo y contraataque")


class EstiloBoca(EstiloJuego):
    def estrategia(self):
        print("Estilo Boca: defensivo y contraataque rápido")

#Abstract Factory
class EquipoFactory:
    def crear_jugador(self):
        pass

    def crear_tecnico(self):
        pass

    def crear_estilo(self):
        pass


class RiverFactory(EquipoFactory):
    def crear_jugador(self):
        return JugadorRiver()

    def crear_tecnico(self):
        return TecnicoRiver()

    def crear_estilo(self):
        return EstiloRiver()


class BocaFactory(EquipoFactory):
    def crear_jugador(self):
        return JugadorBoca()

    def crear_tecnico(self):
        return TecnicoBoca()

    def crear_estilo(self):
        return EstiloBoca()

#Cliente
def simular_equipo(factory):

    jugador = factory.crear_jugador()
    tecnico = factory.crear_tecnico()
    estilo = factory.crear_estilo()

    jugador.jugar()
    tecnico.dirigir()
    estilo.estrategia()

print("RIVER")
simular_equipo(RiverFactory())

print("\nBOCA")
simular_equipo(BocaFactory())