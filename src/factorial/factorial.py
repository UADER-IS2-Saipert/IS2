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

# Verificar si se proporcionó un argumento, de lo contrario solicitar al usuario
if len(sys.argv) == 1:  # No se pasó un argumento
    print("Debe informar un número! Lo solicitamos a continuación.")
    num = int(input("Ingrese un número: "))  # Solicitar al usuario el número
else:
    num = int(sys.argv[1])  # Usar el argumento proporcionado

print(f"Factorial {num}! es {factorial(num)}")
