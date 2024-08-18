"""
Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
"""
def maior_elemento(lista):
    #Variavel que guardara o maior elemento da lista
    maior = lista[0]
    #Laço de repetição que ira iterar pelos elementos da lista
    for elemento in lista:
        #Guarda-se o maior valor entre o elemento e a variavel maior.
        if elemento>maior:
            maior = elemento
    #Retorna-se o valor da soma dos elementos da lista
    return maior