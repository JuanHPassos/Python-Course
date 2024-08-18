"""
Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:

Exemplo 1:

Entrada de Dados:

Digite um número inteiro: 78615

Saída de Dados:

O dígito das dezenas é 1
"""
numero = int(input("Digite um número inteiro: "))
print(f"O dígito das dezenas é {(numero//10)%10}")