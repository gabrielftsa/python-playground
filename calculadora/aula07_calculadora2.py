class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def divisao(self, a, b):
        return a / b

    def multiplicacao(self, a, b):
        return a * b

    
if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(2, 4))
    print(calculadora.divisao(2, 4))
    print(calculadora.multiplicacao(2, 4))
    print(calculadora.subtracao(2, 4))
    print("Fim do programa.")
