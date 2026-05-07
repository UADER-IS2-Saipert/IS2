# =========================
# Bridge
# =========================

class TrenLaminador:

    def producir(self):
        pass

#==========================
# Trenes
#==========================

class Tren5Metros(TrenLaminador):

    def producir(self):
        return "Produciendo planchas de 5 metros para transportar"


class Tren10Metros(TrenLaminador):

    def producir(self):
        return "Produciendo planchas de 10 metros para transportar"
    
# =========================
# Abstract
# =========================

class LaminaAcero:

    def __init__(self, espesor, ancho, tren):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = tren 


    def fabricar(self):

        print(f"Lámina de acero:")
        print(f"Espesor: {self.espesor} pulgadas")
        print(f"Ancho: {self.ancho} metros")

        print(self.tren.producir())
    
# =========================
# Pruebas
# =========================

# Trenes laminadores
tren5 = Tren5Metros()
tren10 = Tren10Metros()

# Láminas enviadas a distintos trenes
lamina1 = LaminaAcero(0.5, 1.5, tren5)
lamina2 = LaminaAcero(0.5, 1.5, tren10)

print("----- Producción 1 -----")
lamina1.fabricar()

print("\n----- Producción 2 -----")
lamina2.fabricar()