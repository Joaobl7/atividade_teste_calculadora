# calculadora.py
class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Erro: Divisão por zero.")
        return a / b

    def potenciacao(self, a, b):
        return a ** b

    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Erro: Raiz quadrada de número negativo.")
        return a ** 0.5

    def media(self, numeros):
        if not numeros:
            raise ValueError("Erro: Lista de números está vazia.")
        total = sum(numeros)
        return total / len(numeros)

    def modulo(self, a):
        return a if a >= 0 else -a

    def percentual(self, parte, total):
        if total == 0:
            raise ValueError("Erro: Total não pode ser zero.")
        return (parte / total) * 100
