"""
Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
"""
def soma_elementos(lista):
    #Variavel que guardara a soma dos elementos
    soma = 0
    #Laço de repetição que ira iterar pelos elementos da lista
    for elemento in lista:
        #Soma recebe a soma atual mais o valor do i-esimo elemento.
        soma = soma + elemento
    #Retorna-se o valor da soma dos elementos da lista
    return soma    