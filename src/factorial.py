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

def validar_rango(num):
    return 2 <= num <= 6

def procesar_entrada(entrada):
    try:
        if "-" in entrada:
            partes = entrada.split("-")
            desde = int(partes[0])
            hasta = int(partes[1])

            if desde > hasta:
                desde, hasta = hasta, desde

            if not (validar_rango(desde) and validar_rango(hasta)):
                print("Error: solo se permiten valores entre 2 y 6.")
                return

            for i in range(desde, hasta + 1):
                print(f"{i}! = {factorial(i)}")

        else:
            num = int(entrada)

            if not validar_rango(num):
                print("Error: solo se permiten valores entre 2 y 6.")
                return

            print(f"{num}! = {factorial(num)}")

    except:
        print("Entrada inválida. Use un número entre 2 y 6.")

if len(sys.argv) < 2:
    entrada = input("Ingrese un número entre 2 y 6: ")
else:
    entrada = sys.argv[1]

procesar_entrada(entrada)