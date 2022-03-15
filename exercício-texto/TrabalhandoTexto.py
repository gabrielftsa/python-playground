import shutil  # o shutil terá uso caso eu queira copiar ou transportar meu aquivo para outro local.


def escrever_arquivo(texto):  # Abro o meu arquivo de texto.
    diretorio = 'C:/Users/gabri/PycharmProjects/app_python/notas.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):  # Escrevo algo sem apagar o que estava escrito anteriormente
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):  # def que vai ler meu arquivo de texto e apresentar na tela o que foi lido
    arquivo = open(nome_arquivo, 'r', encoding='UTF-8')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):  # Aqui serão separados números de letras para serem calculados
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')  # o split está fragmentando o texto sempre que encontrar uma quebra de linha
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in lista_notas]) / 4  # sum faz a soma de todos os números em cada linha
        lista_media.append({aluno: media(lista_media)})
    return lista_media

# def move_arquivo(nome_arquivo): # Exemplo de como seria usado o shutil
#     shutil.move(nome_arquivo, '') # Dentro das aspas simples ficaria o destino do arquivo

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    # aluno = 'Arthur do Val,5,8,1,0\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('notas.txt')
