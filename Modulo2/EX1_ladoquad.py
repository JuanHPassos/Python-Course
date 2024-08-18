"""
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como devem ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados: 

Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:

perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez"""

#Leitura do lado do quadrado
#A função input le um dado do teclado e retorna uma string, a qual é convertida para inteiro, por conta do cast int()
lado = int(input())
#Calculo perimetro(lado vezes 4)
x = lado*4
#Calculo area(lado elevado ao quadrado)
y = lado**2
print(f"perímetro: {x} - área: {y}")