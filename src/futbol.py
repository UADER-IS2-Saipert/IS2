# =========================
# Flyweight
# Datos compartidos
# =========================

class EquipoFlyweight:

    def __init__(self, nombre, camiseta, estadio):

        self.nombre = nombre
        self.camiseta = camiseta
        self.estadio = estadio


    def mostrar_datos(self, jugador, numero):

        print(f"""
Equipo: {self.nombre}
Camiseta: {self.camiseta}
Estadio: {self.estadio}
Jugador: {jugador}
Número: {numero}
""")


# =========================
# Flyweight Factory
# =========================

class FabricaEquipos:

    equipos = {}


    @classmethod
    def obtener_equipo(cls, nombre, camiseta, estadio):

        clave = nombre

        if clave not in cls.equipos:

            cls.equipos[clave] = EquipoFlyweight(
                nombre,
                camiseta,
                estadio
            )

            print(f"Creando equipo: {nombre}")

        return cls.equipos[clave]


# =========================
# Cliente
# =========================

equipo1 = FabricaEquipos.obtener_equipo(
    "River Plate",
    "Blanca y roja",
    "Monumental"
)

equipo1.mostrar_datos("Gonzalo Montiel", 29)


equipo2 = FabricaEquipos.obtener_equipo(
    "Flamengo",
    "Negra y roja",
    "Maracaná"
)

equipo2.mostrar_datos("Nicolas De La Cruz", 11)


equipo3 = FabricaEquipos.obtener_equipo(
    "Chelsea",
    "Azul",
    "Stamford Bridge"
)

equipo3.mostrar_datos("Enzo Fernandez", 8)