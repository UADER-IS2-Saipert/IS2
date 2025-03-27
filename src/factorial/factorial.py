#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys  # Importa el módulo sys para manejar los argumentos de la línea de comandos

# Función para calcular el factorial de un número
def factorial(num): 
    if num < 0:  # Verifica si el número es negativo, ya que el factorial de números negativos no existe
        print("Factorial de un número negativo no existe")
        return 0  # Retorna 0 si el número es negativo
    elif num == 0:  # Si el número es 0, su factorial es 1 por definición
        return 1
    else:  # Si el número es positivo, calcula el factorial utilizando un bucle
        fact = 1
        while(num > 1):  # Mientras el número sea mayor a 1
            fact *= num  # Multiplica el número actual por el factorial acumulado
            num -= 1  # Decrementa el número
        return fact  # Retorna el resultado final del factorial

# Verifica si el programa fue ejecutado sin argumentos de línea de comandos
if len(sys.argv) == 1:  # Si no se pasó ningún argumento en la línea de comandos
    print("Debe informar un número o un rango! Lo solicitamos a continuación.")
    # Solicita al usuario que ingrese un número o un rango
    user_input = input("Ingrese un número, un rango (ejemplo 4-8), '-hasta' (ejemplo -10) o 'desde-' (ejemplo desde-5): ")
    
    # Si el usuario ingresó un rango con guion
    if '-' in user_input:
        if user_input.startswith('desde-'):  # Si el rango comienza con 'desde-', se calcula desde ese número hasta 60
            start = int(user_input[6:])  # Elimina 'desde-' y convierte el resto a un número entero
            for i in range(start, 61):  # Calcula el factorial desde 'start' hasta 60
                print(f"Factorial de {i}! es {factorial(i)}")
        elif user_input.startswith('-'):  # Si el rango comienza con '-', se calcula desde 1 hasta el número indicado
            end = int(user_input[1:])  # Elimina el '-' y convierte el resto a un número entero
            for i in range(1, end + 1):  # Calcula el factorial desde 1 hasta 'end'
                print(f"Factorial de {i}! es {factorial(i)}")
        else:  # Si el usuario ingresó un rango con dos números separados por '-', se calcula el factorial en ese rango
            start, end = map(int, user_input.split('-'))  # Divide el rango y convierte ambos valores a enteros
            for i in range(start, end + 1):  # Calcula el factorial de cada número en el rango
                print(f"Factorial de {i}! es {factorial(i)}")
    else:  # Si el usuario solo ingresó un número, calcula su factorial
        num = int(user_input)  # Convierte la entrada del usuario a un número entero
        print(f"Factorial {num}! es {factorial(num)}")

else:  # Si se pasó un argumento en la línea de comandos
    input_value = sys.argv[1]  # Toma el primer argumento

    # Si el argumento contiene un rango con guion
    if '-' in input_value:
        if input_value.startswith('desde-'):  # Si el rango comienza con 'desde-', se calcula desde ese número hasta 60
            start = int(input_value[6:])  # Elimina 'desde-' y convierte el resto a un número entero
            for i in range(start, 61):  # Calcula el factorial desde 'start' hasta 60
                print(f"Factorial de {i}! es {factorial(i)}")
        elif input_value.startswith('-'):  # Si el rango comienza con '-', se calcula desde 1 hasta el número indicado
            end = int(input_value[1:])  # Elimina el '-' y convierte el resto a un número entero
            for i in range(1, end + 1):  # Calcula el factorial desde 1 hasta 'end'
                print(f"Factorial de {i}! es {factorial(i)}")
        else:  # Si el argumento es un rango con dos números, calcula los factoriales en ese rango
            start, end = map(int, input_value.split('-'))  # Divide el rango y convierte ambos valores a enteros
            for i in range(start, end + 1):  # Calcula el factorial de cada número en el rango
                print(f"Factorial de {i}! es {factorial(i)}")
    else:  # Si el argumento es un solo número, calcula su factorial
        num = int(input_value)  # Convierte el argumento a un número entero
        print(f"Factorial {num}! es {factorial(num)}")
