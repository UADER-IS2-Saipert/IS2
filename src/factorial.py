#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función que calcula el factorial de un número
def factorial(num): 
    # Factorial de negativo no existe
    if num < 0: 
        print(f"Factorial de {num} no existe")
        return None
    # Caso base
    elif num == 0: 
        return 1
    else: 
        fact = 1
        # Cálculo iterativo del factorial
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Función que interpreta la entrada del usuario
def procesar_entrada(entrada):
    try:
        # Si la entrada contiene "-", puede ser un rango
        if "-" in entrada:
            partes = entrada.split("-")

            # Caso "-hasta" desde 1 hasta el número indicado
            if partes[0] == "":
                desde = 1
                hasta = int(partes[1])  # conversión a entero

            # Caso "desde-" desde el número indicado hasta 60
            elif partes[1] == "":
                desde = int(partes[0])  # conversión a entero
                hasta = 60

            # Caso "desde-hasta"
            else:
                desde = int(partes[0])  # conversión a entero
                hasta = int(partes[1])  # conversión a entero

            # Si los valores están invertidos, se corrigen
            if desde > hasta:
                desde, hasta = hasta, desde

            # Se calculan los factoriales en el rango
            for i in range(desde, hasta + 1):
                print(f"{i}! = {factorial(i)}")

        else:
            # Caso de número único
            num = int(entrada)  # conversión a entero
            print(f"{num}! = {factorial(num)}")

    # Manejo de errores de entrada
    except:
        print("Entrada inválida.")

# Obtiene entrada por argumento o teclado
if len(sys.argv) < 2:
    # Si no se pasa argumento, se solicita al usuario
    entrada = input("Ingrese un número o rango (ej: 2-6, -10, 5-): ")
else:
    # Si se pasa argumento, se usa directamente
    entrada = sys.argv[1]

# Se procesa la entrada
procesar_entrada(entrada)