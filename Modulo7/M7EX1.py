"""
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída."""
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
            #Imprimi "#" sem "\n", lado a lado.
            print("#", end="")
            j = j +1
        #Pula a linha para formar a proxima.
        print()
        i = i+1 
    
main()
