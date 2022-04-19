import random
import string

print("-"*19, "BEM-VINDO(A) AO GERADOR DE SENHAS.", "-"*19)
print("-> Responda estes 2 passos importantes para que tudo fique como você quer.")
resposta = str(input("\nVocê aprova a possibilidade de ter 'ç' em sua senha? (s/n): "))
tamanho = int(input("Nos diga a quantidade de dígitos que você deseja em sua senha: "))

if resposta == "s":
    chars = string.ascii_letters + string.digits + "ç!@#$%&?:"
elif resposta == "n":
    chars = string.ascii_letters + string.digits + "!@#$%&?:"

rnd = random.SystemRandom()  # os.urandom
senhagerada = "".join(rnd.choice(chars) for i in range(tamanho))

if __name__ == '__main__':
    print("\nAqui está sua senha: {}".format(senhagerada))
