"""
Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, h é uma hipotenusa se existem números inteiros i e j tais que:

h^2 = i^2 + j^2

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

Dica 1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica 2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

"""
#Função para verificar se é hipotenusa
def e_hipotenusa(c):
    #Testar todas as combinacoes até a == c
    #a = cateto e c é a hipotenusa
    a = 1
    while a<c:
        #Inicia-se "b" como "a" para evitar repetição de combinações
        #b = cateto
        b = a
        while b<c:
            if(c**2 == a**2+b**2):
                #Se for hipotenusa, retorna verdadeiro
                return True
            b = b+1
        a = a+1
    #Se o codigo chegar ate aqui, nao eh hipotenusa
    return False
#Função que calcula soma das hipotenusas
def soma_hipotenusas(n):
    #Variavel resposta
    ans = 0
    #Primeira hipotenusa inteira
    i = 5
    #Chegar todos os numeros de i ate n
    while i<=n:
        if(e_hipotenusa(i)):
            #Se for primo, adiciona a soma
            ans = ans + i
        i = i+1
    #Retorna a soma das hipotenusas
    return ans