"""
Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
"""

def main():
    #Leitura dos dados.
    m = int(input("digite a largura: "))
    n = int(input("digite a altura: "))
    i = 0
    #Percorre as linhas.
    while i<n:
        j = 0
        #Percorre as colunas.
        while j<m:
           #Se estiver na borda 
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                #Imprimi "#" sem "\n", lado a lado.
                print("#", end="")
            #Se estiver no meio, preenche-se com espaço
            else:
                print(" ", end="")
            #Avança para próxima coluna
            j = j +1
        #Pula a linha para formar a proxima.
        print()
        #Avança para a proxima linha.
        i = i+1 
    
main()