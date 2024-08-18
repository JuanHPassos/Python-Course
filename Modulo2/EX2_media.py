"""
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:

Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:

A média aritmética é 5.5

"""
#Leitura de dados 
a = float(input("Digite a primeira nota:"))
b = float(input("Digite a segunda nota:"))
c = float(input("Digite a terceira nota:"))
d = float(input("Digite a quarta nota:"))
#Atribuição
media = (a+b+c+d)/4
#Impressão da media
print("A média aritmética é", media)