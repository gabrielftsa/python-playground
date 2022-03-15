print("Digite as notas de cada bimestre e a média será calculada.")
n1 = int(input("Primeiro bimestre: "))
while n1 > 10:
    n1 = int(input("Algo saiu errado. Digite a nota do primeiro bimestre: "))
n2 = int(input("Segundo Bimestre: "))
while n2 > 10:
    n2 = int(input("Algo saiu errado. Digite a nota do segundo bimestre: "))
n3 = int(input("Terceiro bimestre: "))
while n3 > 10:
    n3 = int(input("Algo saiu errado. Digite a nota do terceiro bimestre: "))
n4 = int(input("Quarto bimestre: "))
while n4 > 10:
    n4 = int(input("Algo saiu errado. Digite a nota do quarto bimestre: "))
media = (n1 + n2 + n3 + n4) / 4
print(f"A média do aluno é: {media}")
