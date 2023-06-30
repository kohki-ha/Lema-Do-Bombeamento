import random


def pegar_palavra_aleatoria(linguagem):
    palavras = sorted(linguagem, key=len)[2:]
    palavra = random.choice(palavras)
    return palavra



def lema_do_bombeamento(linguagem, palavra):
    tamanho_palavra = len(palavra)

    if tamanho_palavra < 3:
        resultado = "A palavra não possui tamanho suficiente para aplicar o Lema do Bombeamento.\n"
    elif tamanho_palavra % 2 == 0:
        resultado = "A palavra possui um número par de caracteres, portanto, não é possível aplicar o Lema do Bombeamento.\n"
    else:
        n = (tamanho_palavra - 1) // 2

        u = palavra[:n]
        v = palavra[n]
        z = palavra[n + 1:]

        palavra_teste = u + v + v + z

        if palavra_teste in linguagem:
            resultado = "A linguagem pode ser uma linguagem regular.\n"
        else:
            resultado = "A linguagem NÃO é uma linguagem regular.\n"

    print(resultado)


def main():
    linguagem = {('0'*n + '1'*n + '2'*n) for n in range(50)}

    palavra = pegar_palavra_aleatoria(linguagem)

    print("Linguagem: {}".format(sorted(linguagem, key=len)))
    print("\nPalavra aleatória: {}\n".format(palavra))
    lema_do_bombeamento(linguagem, palavra)


main()
