import matplotlib.pyplot as plt

def collatz_iteraciones(n):
    iteraciones = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1

    return iteraciones


def calcular_collatz(rango_max):
    numeros = []
    iteraciones = []

    for i in range(1, rango_max + 1):
        numeros.append(i)
        iteraciones.append(collatz_iteraciones(i))

    return numeros, iteraciones


def graficar(numeros, iteraciones):
    plt.figure()

    plt.scatter(iteraciones, numeros, s=1)

    plt.xlabel("Cantidad de iteraciones")
    plt.ylabel("Número inicial (n)")
    plt.title("Conjetura de Collatz (1 a 10000)")

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    rango = 10000
    numeros, iteraciones = calcular_collatz(rango)
    graficar(numeros, iteraciones)