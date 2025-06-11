import random
from termcolor import colored

with open('palavras5letras.txt', 'r') as arquivo:
    lista_palavras = [linha.strip() for linha in arquivo]

def inicio():
    print("\n<<<<Bem Vindo ao Termo!>>>>\n"
          "Como Jogar:\n"
          "Você terá 6 chances para descobrir a palavra secreta.\n"
          "A cada tentativa as letras mudarão de cor, indicando sua posição na palavra a ser descoberta.\n"
          "Caso a letra mudar para a cor verde, ela está na posição correta.\n"
          "Caso a letra mudar para a cor amarela, ela existe na palavra secreta mas está na posição incorreta.\n"
          "Por fim se a letra não mudar de cor, ela não existe na palavra secreta.\n"
          "Bom jogo!!!\n")


def verificador():
    while True:
        palavra_usuario = input("Digite uma palavra de 5 letras\n").strip()

        if palavra_usuario not in lista_palavras:
            print("\nPalavra inválida, tente novamente!\n")
        else:
            return palavra_usuario

def cor_letras(palavra, palavra_secreta):
    contador = list(palavra_secreta)
    resultado = []

    for i in range(5):
            if palavra[i] == palavra_secreta[i]:
                resultado.append(colored(palavra[i], 'green'))
                contador.remove(palavra[i])

            else:
                resultado.append(colored(palavra[i], 'white'))

    for j in range(5):
        if palavra[j] in contador:
                resultado[j] = (colored(palavra[j], 'yellow'))
                contador.remove(palavra[j])

    resultado = ''.join(resultado)
    return resultado

def main():
    palavra_secreta = random.choice(lista_palavras)
    tentativas = 0
    inicio()

    while tentativas != 6:
        print("Tentativa: ", tentativas+1)
        palavra = verificador()
        res = cor_letras(palavra,palavra_secreta)
        print(res,"\n")
        tentativas += 1

        if palavra == palavra_secreta:
            print("Parabéns você acertou a palavra secreta!!!")
            break
        elif tentativas == 6 and palavra != palavra_secreta:
            print("Máximo de tentativas alcançada, tente novamente mais tarde.\n"
            "A palavra secreta era ",palavra_secreta)
        
main()
