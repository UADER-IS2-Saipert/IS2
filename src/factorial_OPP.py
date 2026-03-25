import sys

# Clase que encapsula la lógica del cálculo de factorial
class Factorial:

    # Constructor
    def __init__(self):
        pass

    # Método para calcular el factorial de un número
    def factorial(self, num):
        if num < 0:
            print(f"Factorial de {num} no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    # Método principal que calcula factoriales en un rango
    def run(self, minimo, maximo):
        # Corrige si el rango viene invertido
        if minimo > maximo:
            minimo, maximo = maximo, minimo

        # Recorre el rango y calcula factoriales
        for i in range(minimo, maximo + 1):
            print(f"{i}! = {self.factorial(i)}")


# Función para interpretar entrada
def procesar_entrada(entrada):
    try:
        if "-" in entrada:
            partes = entrada.split("-")

            if partes[0] == "":
                minimo = 1
                maximo = int(partes[1])
            elif partes[1] == "":
                minimo = int(partes[0])
                maximo = 60
            else:
                minimo = int(partes[0])
                maximo = int(partes[1])
        else:
            minimo = maximo = int(entrada)

        # Crear objeto y ejecutar
        f = Factorial()
        f.run(minimo, maximo)

    except:
        print("Entrada inválida.")


# Programa principal
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango.: ")
else:
    entrada = sys.argv[1]

procesar_entrada(entrada)