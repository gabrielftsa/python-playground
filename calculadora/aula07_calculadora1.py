class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

    def multiplicacao(self):
        return self.a * self.b


if __name__ == '__main__':
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    calculadora = Calculadora(n1, n2)
    print(f"Seus números são: {n1} e {n2}")
    print(calculadora.soma())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())
    print(calculadora.subtracao())
    print("Fim do programa.")
