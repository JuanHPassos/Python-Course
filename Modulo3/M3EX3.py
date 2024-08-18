"""
Receba um número inteiro na entrada e imprima Buzz se o número for divisível por 5.
Caso contrário, imprima o mesmo número que foi dado na entrada.
"""
n = int(input())
if n%5:
    print(n)
else:
    print("Buzz")
    