#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
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

# Verificar si el argumento es un rango (ej. 4-8) o un solo número
if len(sys.argv) == 1:  # No se pasó un argumento
    print("Debe informar un número o un rango! Lo solicitamos a continuación.")
    user_input = input("Ingrese un número o un rango (ejemplo 4-8): ")
    
    # Verificar si el usuario ingresó un rango
    if '-' in user_input:
        start, end = map(int, user_input.split('-'))
        for i in range(start, end + 1):
            print(f"Factorial de {i}! es {factorial(i)}")
    else:
        num = int(user_input)
        print(f"Factorial {num}! es {factorial(num)}")

else:  # Se pasó un argumento
    input_value = sys.argv[1]
    
    # Verificar si el argumento es un rango (ej. 4-8)
    if '-' in input_value:
        start, end = map(int, input_value.split('-'))
        for i in range(start, end + 1):
            print(f"Factorial de {i}! es {factorial(i)}")
    else:
        num = int(input_value)
        print(f"Factorial {num}! es {factorial(num)}")
