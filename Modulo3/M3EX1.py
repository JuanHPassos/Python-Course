"""
Receba um número inteiro na entrada e imprima par quando o número for par ou 
ímpar quando o número for ímpar."""
n = int(input())
#Se n resto 2 entrar no if, entao há resto, logo é ímpar.
if n%2:
    print("ímpar")
else:   
    print("par")
