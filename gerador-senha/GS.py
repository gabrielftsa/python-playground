import time
import random
import string
import pyperclip as pc

print("-" * 19, "BEM-VINDO(A) AO GERADOR DE SENHAS.", "-" * 19)
print("-> Responda estes 2 passos importantes para que tudo fique como você quer.")

resposta1 = str(input("\n1°) Você aprova a possibilidade de ter 'ç' em sua senha? (s/n): "))
while resposta1 != 's' and resposta1 != 'n':
    print("Responda apenas com 's' para SIM ou 'n' para NÃO.")
    resposta1 = str(input("Você aprova a possibilidade de ter 'ç' em sua senha? (s/n): "))

if resposta1 == "s":
    chars = string.ascii_letters + string.digits + "ç!@#$%&?:"
elif resposta1 == "n":
    chars = string.ascii_letters + string.digits + "!@#$%&?:"

tamanho = int(input("2°) Nos diga a quantidade de dígitos que você deseja em sua senha (máx: 30): "))
while tamanho > 30 or tamanho <= 0:
    print("O número máximo de dígitos foi excedido. Tente novamente.")
    tamanho = int(input("Nos diga a quantidade de dígitos que você deseja em sua senha (máx 30): "))

rnd = random.SystemRandom()  # os.urandom
print("\nGerando senha...")
time.sleep(1)
senhagerada = "".join(rnd.choice(chars) for i in range(tamanho))

if __name__ == '__main__':
    print("\nAqui está sua senha: {}".format(senhagerada))
    resposta2 = str(input("\nDeseja copiar sua senha gerada? (s/n)"))
    while resposta2 != 's' and resposta2 != 'n':
        print("Responda apenas com 's' para SIM ou 'n' para NÃO.")
        resposta2 = str(input("Deseja copiar sua senha gerada? (s/n)"))
    if resposta2 == 's':
        pc.copy(senhagerada)
        print("Senha copiada com sucesso! Agradecemos pela preferência. Volte sempre :) ")
    else:
        print("Sem problemas. Agradecemos pela preferência. Volte sempre :)")
    input()
