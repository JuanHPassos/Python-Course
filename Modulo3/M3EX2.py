""""
Receba um número inteiro na entrada e imprima Fizz se o número for divisível por 3.
Caso contrário, imprima o mesmo número que foi dado na entrada.
 """
n = int(input())
#Se houver resto, nao é divisel por 3, e adentrará o if, printando o numero de entrada
if n%3:
    print(n)
else:
    print("Fizz")
    