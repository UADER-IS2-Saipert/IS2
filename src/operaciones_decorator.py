# =========================
# Componente
# =========================

class Numero:

    def operar(self):
        pass


# =========================
# Componente Concreto
# =========================

class ValorBase(Numero):

    def __init__(self, valor):

        self.valor = valor


    def operar(self):

        return self.valor


# =========================
# Decorator Base
# =========================

class DecoratorNumero(Numero):

    def __init__(self, numero):

        self.numero = numero


# =========================
# Decoradores Concretos
# =========================

class SumarDos(DecoratorNumero):

    def operar(self):

        return self.numero.operar() + 2

class MultiplicarPorDos(DecoratorNumero):

    def operar(self):

        return self.numero.operar() * 2

class DividirPorTres(DecoratorNumero):

    def operar(self):

        return self.numero.operar() / 3


# =========================
# Pruebas
# =========================

numero = ValorBase(9)

print("Valor original:", numero.operar())

numero1 = SumarDos(numero)
print("Sumarle 2:", numero1.operar())

numero2 = MultiplicarPorDos(numero1)
print("Multiplicar por 2:", numero2.operar())

numero3 = DividirPorTres(numero2)
print("Dividir por 3:", numero3.operar())