"""
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
"""
#Funcao que verifica se um numero é primo

def n_primos(n):
    #Variavel que fará as iterações
    i = 2
    #Variavel que conta o numeros primos
    ans = 0
    #Verificar todos os numeros de 2 a n
    while i != n:
        #Se o numero for primo
        if(ePrimo(i)):
            #Acrecenta na resposta
            ans = ans + 1
        i = i+1
    #Retorno da quantidade de primos
    return ans

def ePrimo(n):
    i = 2
    #Confere se o numero possui divisores
    while i <= n/2:
        #Se possui, nao é primo
        if not n%i:
            return False
        #Verificar proximo numero
        i = i+1
    #Se o programa chegar ate aqui, o numero nao tem divisores
    return True