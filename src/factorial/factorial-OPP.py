#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys  # Importamos el módulo sys para manejar los argumentos de la línea de comandos

# Definimos la clase Factorial
class Factorial:
    # Constructor de la clase, donde inicializamos los valores de min y max
    def __init__(self, min_val=1, max_val=10):
        self.min_val = min_val
        self.max_val = max_val

    # Método que calcula el factorial de un número
    def factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact

    # Método que ejecuta el cálculo de factorial entre el rango min y max
    def run(self):
        # Itera desde min_val hasta max_val, calculando el factorial de cada número
        for i in range(self.min_val, self.max_val + 1):
            print(f"Factorial de {i}! es {self.factorial(i)}")

# Si el programa es ejecutado desde la línea de comandos, maneja los argumentos
if __name__ == "__main__":
    # Verifica si el programa fue ejecutado sin argumentos
    if len(sys.argv) == 1:
        # Solicita al usuario ingresar un rango
        user_input = input("Ingrese un rango (ejemplo 4-8): ")

        # Verifica si el rango ingresado está en el formato adecuado (min-max)
        if '-' in user_input:
            start, end = map(int, user_input.split('-'))
            # Crea una instancia de la clase Factorial con el rango especificado
            factorial_calculator = Factorial(start, end)
            # Ejecuta el cálculo de factorial para el rango dado
            factorial_calculator.run()
        else:
            print("Entrada inválida. Por favor, ingrese un rango válido.")
    else:
        # Si el programa fue ejecutado con argumentos, usará esos valores
        input_value = sys.argv[1]
        if '-' in input_value:
            start, end = map(int, input_value.split('-'))
            factorial_calculator = Factorial(start, end)
            factorial_calculator.run()
        else:
            print("Entrada inválida. El formato debe ser min-max.")
