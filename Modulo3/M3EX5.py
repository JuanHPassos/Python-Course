"""
Receba 3 números inteiros na entrada e imprima crescente
se eles forem dados em ordem crescente. Caso contrário, imprima
não está em ordem crescente"""
a = int(input())
b = int(input())
c = int(input())
#Se a for menor igual a b e b for menor igual a c, sabe-se que a é menor igual a c, entao esta na ordem crescente
if a <= b and b <= c:
    print("crescente")
else:
    print("não está em ordem crescente")     