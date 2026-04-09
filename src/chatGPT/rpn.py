# =========================================
# Calculadora RPN (Notación Polaca Inversa)
# =========================================

import sys
import math

# =========================
# Excepción personalizada
# =========================
class RPNError(Exception):
    """Excepción específica para errores de la calculadora RPN"""
    pass


# =========================
# Clase Pila RPN
# =========================
class Pila:
    """Clase que representa la pila y operaciones RPN"""

    def __init__(self):
        """Inicializa la pila y 10 memorias (00-09)"""
        self.stack = []
        self.memoria = {f"{i:02}": 0 for i in range(10)}

    def push(self, x):
        """Inserta número o constante en la pila"""
        if isinstance(x, str):
            x = x.lower()
            if x == 'pi':
                x = math.pi
            elif x == 'e':
                x = math.e
            elif x == 'phi':
                x = (1 + 5**0.5) / 2
            else:
                try:
                    x = float(x)
                except ValueError:
                    raise RPNError(f"Entrada inválida: {x}")
        self.stack.append(x)

    def pop(self):
        """Extrae elemento superior de la pila"""
        if not self.stack:
            raise RPNError("Pila vacía")
        return self.stack.pop()

    def operacion_binaria(self, func):
        """Aplica operación binaria a los dos elementos superiores"""
        if len(self.stack) < 2:
            raise RPNError("Faltan operandos")
        b = self.pop()
        a = self.pop()
        try:
            self.push(func(a, b))
        except ZeroDivisionError:
            raise RPNError("División por cero")

    def operacion_unaria(self, func, dominio=None):
        """Aplica operación unaria al tope de la pila"""
        if not self.stack:
            raise RPNError("Pila vacía")
        x = self.pop()
        if dominio and not dominio(x):
            raise RPNError("Error de dominio")
        self.push(func(x))

    # =========================
    # Comandos de pila
    # =========================
    def dup(self):
        """Duplica el elemento superior"""
        if not self.stack:
            raise RPNError("Pila vacía")
        self.stack.append(self.stack[-1])

    def swap(self):
        """Intercambia los dos elementos superiores"""
        if len(self.stack) < 2:
            raise RPNError("Faltan operandos")
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def drop(self):
        """Elimina el tope"""
        self.pop()

    def clear(self):
        """Vacía completamente la pila"""
        self.stack.clear()

    def chs(self):
        """Cambia el signo del tope (+/-)"""
        if not self.stack:
            raise RPNError("Pila vacía")
        self.stack[-1] = -self.stack[-1]

    # =========================
    # Memoria
    # =========================
    def sto(self, k):
        """Guarda el tope en memoria (consume el tope)"""
        if not self.stack:
            raise RPNError("Pila vacía")
        if k not in self.memoria:
            raise RPNError("Memoria inválida")
        self.memoria[k] = self.pop()

    def rcl(self, k):
        """Recupera valor de memoria y lo coloca en la pila"""
        if k not in self.memoria:
            raise RPNError("Memoria inválida")
        self.stack.append(self.memoria[k])


# =========================
# Evaluador RPN
# =========================
def evaluar(expr):
    """
    Evalúa una expresión RPN y devuelve el resultado
    Lanza RPNError en caso de error
    """
    if not expr.strip():
        raise RPNError("Expresión vacía")

    pila = Pila()
    tokens = expr.split()

    # Diccionario de operaciones
    ops = {
        '+': lambda: pila.operacion_binaria(lambda a, b: a + b),  # suma
        '-': lambda: pila.operacion_binaria(lambda a, b: a - b),  # resta
        '*': lambda: pila.operacion_binaria(lambda a, b: a * b),  # multiplicación
        '/': lambda: pila.operacion_binaria(lambda a, b: a / b),  # división
        'yx': lambda: pila.operacion_binaria(lambda a, b: a ** b),  # potencia
        '1/x': lambda: pila.operacion_unaria(lambda x: 1 / x, lambda x: x != 0),  # inverso
        'chs': pila.chs,  # cambia signo
        'dup': pila.dup,  # duplica
        'swap': pila.swap,  # intercambia
        'drop': pila.drop,  # elimina
        'clear': pila.clear,  # vacía pila
        'sqrt': lambda: pila.operacion_unaria(math.sqrt, lambda x: x >= 0),  # raíz cuadrada
        'log': lambda: pila.operacion_unaria(math.log10, lambda x: x > 0),  # logaritmo base 10
        'ln': lambda: pila.operacion_unaria(math.log, lambda x: x > 0),  # logaritmo natural
        'exp': lambda: pila.operacion_unaria(math.exp),  # exponencial
        '10x': lambda: pila.operacion_unaria(lambda x: 10**x),  # 10^x
        'sin': lambda: pila.operacion_unaria(lambda x: math.sin(math.radians(x))),  # seno
        'cos': lambda: pila.operacion_unaria(lambda x: math.cos(math.radians(x))),  # coseno
        'tg': lambda: pila.operacion_unaria(lambda x: math.tan(math.radians(x))),  # tangente
        'asin': lambda: pila.operacion_unaria(lambda x: math.degrees(math.asin(x)), lambda x: -1 <= x <= 1),  # arcsin
        'acos': lambda: pila.operacion_unaria(lambda x: math.degrees(math.acos(x)), lambda x: -1 <= x <= 1),  # arccos
        'atan': lambda: pila.operacion_unaria(lambda x: math.degrees(math.atan(x))),  # arctan
    }

    i = 0
    while i < len(tokens):
        tok = tokens[i]

        if tok in ops:
            ops[tok]()
        elif tok.upper() == 'STO':
            i += 1
            if i >= len(tokens):
                raise RPNError("STO requiere memoria")
            pila.sto(tokens[i])
        elif tok.upper() == 'RCL':
            i += 1
            if i >= len(tokens):
                raise RPNError("RCL requiere memoria")
            pila.rcl(tokens[i])
        else:
            pila.push(tok)

        i += 1

    if len(pila.stack) != 1:
        raise RPNError(f"Resultado inválido: {len(pila.stack)} elementos")

    return pila.pop()


# =========================
# Interfaz CLI
# =========================
def main():
    """Ejecuta la calculadora desde CLI"""
    try:
        expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else (
            input("RPN: ") if sys.stdin.isatty() else sys.stdin.read()
        )
        print(evaluar(expr))
    except RPNError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()

# =========================
# Autor: David Saipert, 2026
# Curso: Ingeniería de Software II
# =========================================