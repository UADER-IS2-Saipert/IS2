import matplotlib.pyplot as plt

# Función para calcular el número de iteraciones de Collatz
def collatz_iterations(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:  # Si es par
            n = n // 2
        else:  # Si es impar
            n = 3 * n + 1
        iterations += 1
    return iterations

# Lista para almacenar los resultados
numbers = []
iterations = []

# Calcular las iteraciones para los números entre 1 y 10000
for n in range(1, 10001):
    numbers.append(n)
    iterations.append(collatz_iterations(n))

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(numbers, iterations, s=1, color='blue', alpha=0.5)
plt.title("Número de iteraciones de Collatz para los números de 1 a 10000")
plt.xlabel("Número de inicio (n)")
plt.ylabel("Número de iteraciones")
plt.grid(True)
plt.savefig('src/collatz_iterations.png')  # Guardar el gráfico en la carpeta src
plt.show()
