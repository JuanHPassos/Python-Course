"""
operações basicas
soma(+)
prioridade(parenteses)
potenciação(**)
comparação(==)
diferente(!=)
divisão real(/)
divisão inteira(//)
Resto divisao(%)
Python obdece ordem de precedencia.

-Definir variaveis:
Tipo inteiro:
x = 5
y=10*32+x
x = 345(5 some)
x = x+10(x == 355)
soma = x+y(soma == 680)
print(soma) -> 680
soma -> 680(note que as duas maneiras servem)
Tipo string
frase = Python e muito facil
exemplo de codigo:
a = 10
b = 20
soma = a+b
print("A soma vale", soma)

Tipos das vairaveis:
type(10) saida:<class 'int'>
type(ola) saida:<class 'str'>
type(5/2) saida:<class 'float'>

Cast em python:
altura = 1.88
alturoint = int(altura)

Tam string:
texto = "bom dia"
len(texto) -> 7(apenas tipo string)
porem pode-se converter tipos.

Entrada de dados:
Programa em python para converter F -> C:
tempF = input("Digite a tempertura em Fahrenheit: ")
tempC = (float(tempF)-32)*5/9
print("Temperatura em Celsius é", tempC)
A função input retorna uma string do que foi digitado, logo é necessário fazer o cast.

OBS: Em python a expressao print ("olá" 'mundo'), imprime olámundo, haja vista que aspas duplas e simples tem a mesma função.

Comando input em + de uma variavel:
a, b, c, d = map(int, input()).split()
nessa linha e lido 4 dados, que sao retornados como uma strig, o split quebra essa string em 4 e o map, faz o cast de cada parte.
Comando print:
Quando você usa o comando print para imprimir mais de uma coisa, ele inclui automaticamente espaços entre os argumentos impressos. Cuidado para não incluir espaços demais na sua resposta! O corretor perceberá e tirará pontos
>>>print("uma coisa", "outra coisa")
uma coisa outra coisa
>>>print("aqui tem ", 2, "espaços")
aqui tem  2 espaços
Assim para eu imprimir por exemplo "perímetro: x - área: y"
eu teria que fazer:
1)print("perímetro:" + str(x) + "-área:" + str(y))
2)print(f"perímetro:{perimetro}-área:{area}")
3)print("perímetro:{}-área:{}".format(perimetro, area))

"""
