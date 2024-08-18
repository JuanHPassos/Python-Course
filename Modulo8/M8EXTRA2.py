"""
Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
"""
#Função para criar lista
def criar_lista():
    #Declara-se uma lista nula
    lista = []
    #Primeira entrada do usuario
    x = int(input("Digite um número: "))
    #Pedir numeros ate x for igual a 0
    while x:
        #Adiciona o valor de x na lista
        lista.append(x)
        #Digite outro numero
        x = int(input("Digite um número: "))
    #Retorna a lista criada e preenchida
    return lista

#Funcao que imprimi uma lista
def imprimi_lista(lista):
    #n recebe a quantidade de elementos da lista
    n = len(lista)
    #Espaço necesário para formatar a saida.
    print()
    #Do ultimo elemento da lista, ate o primeiro, um a um, imprima os elementos.
    for i in range(n-1, -1, -1):
        print(lista[i])

#Funcao principal - chama funçoes
def main():
    #Lista da main, aponta para a lista criada na função
    lista = criar_lista()
    #Função criada para imprimir a lista, tendo-a como parametro 
    imprimi_lista(lista)
    
#Chamada da função principal, para iniciar o codigo. É implementada no final, para o interpretador conheça as funções que serão chamdas    
main()