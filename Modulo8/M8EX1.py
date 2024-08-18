'''
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
'''
def remove_repetidos(lista):
    #Organiza a lista sem gerar uma nova, deixando os elementos repetidos lado lado
    lista.sort()
    #Descobre-se o tamanho da lista
    n = len(lista)
    #Variavel auxiliar para percorrer os elementos
    ptr = 0
    #Iterações para chegar os elementos 2 a 2.
    #!!Como checa-se lista[ptr+1], ptr nao pode assumir n-1!!!
    while ptr<n-1:
        #Se forem iguais, exclui um
        if(lista[ptr] == lista[ptr+1]):
            del lista[ptr]
            #Se um elemento foi excluido, entao o tamanho da lista diminuiu
            n = n-1
        #Caso nao seja, verica-se os proximos
        else:
            ptr = ptr + 1
    #Retorna-se a lista sem repetição
    return lista