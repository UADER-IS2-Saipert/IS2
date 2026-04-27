class EstadioRiver:
    __instancia = None  # Variable que guarda la única instancia

    def __new__(cls):
        # Si todavía no existe una instancia, se crea
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            # Inicializamos atributos una sola vez
            cls.__instancia.nombre = "Estadio Monumental"
            cls.__instancia.capacidad = 85015
        return cls.__instancia  # Siempre devuelve la misma instancia

# Creamos "dos" objetos
estadio1 = EstadioRiver()
estadio2 = EstadioRiver()

# Mostramos datos
print(estadio1.nombre, estadio1.capacidad)

# Verificamos que son el mismo objeto
print(estadio1 is estadio2)  # True