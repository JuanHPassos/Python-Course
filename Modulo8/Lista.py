"""
Listas:
Coleção de objetos(array/vetor)
Exemplo:
playlist = ["Final de semana no parque", "As rosas nao falam"]
lis = [2,3,4,5,6]
>>> playlist[0]
'Final de semana no parque'
Em python numeros negativos pegam o final da lista.
Exemplo:
>>> lis[-1]
6
Lista primos:
primos = [2...97] (primos menores que 100).
>>> len(primos)
25
Lista pode possuir diferentes elementos
Função append:
Concatena ao final da lista um elemento.
Exemplo:
playlist.append("Negro Drama")
>>>playlist
["Final de semana no parque", "As rosas nao falam", "Negro Drama"]
Lista vazia:
vazio = []
Troca elementos:
lis[0] = "oi" 
>>>lis[0]
'oi'
Comando for:
for item in lista:
    comando
Exemplos:
frutas_exoticas = ["jaboticaba","cupuaçu","graviola"]
>>>for fruta in frutas_exoticas:
     print("eu adoro" + fruta)
    
Output:
Eu adoro jaboticaba
Eu adoro cupuaçu
Eu adoro graviola

-Intervalo
range(20)
cria objeto que começa no 0 e vai ate o 20
for i in range(fim):
    comando
for i in range(ini, fim):
    comando
for i in range(ini, fim, passo):
    comando
!!!O for nao chega no final, o i maximo é fim-1!!!
pares = range(0,40,2)
for i in pares: print(i)
imprimi numeros pares entre 0 e 40
Passo negativo
numeros = range(100, 0, -5)

for x in numeros: print(x)

Manipulação de listas:
-Fatias de listas
lis = [0,1,2,3,4,5,6]

>>> lis[1:2]
[1], quantida é igual a final - inicial, pegando sempre o primeiro elemento e nao o ultimo
Esse metodo cria uma nova lista.
Se o intervalo começar  do 0, uma notação adequada é:
>>> lis[:5]
[0,1,2,3,4]
>>> lis[5:]
[5,6]

-Clonando listas:
lis1 = [0,1,2,3,4,5]
list2 = lista1
>>> list2
[0,1,2,3,4,5]
list[0] = 10
>>> list2[0]
10
Nota-se que a alteração de uma lista, afetou a outra e dessa forma, percebe-se que nao foi criado uma nova lista, ambas se referem a mesma lista. 
obs: lista1 e lista2 apontam para essa lista
Como clonar??
def clone(lista):
    clona = []
    for objeto in lista:
        clona.append(objeto)
    return clone
    
Cabe ressalter que o fatiamento CRIA UMA NOVA LISTA.
lista1[:] -> devolve clone da lista

Pertinencia a uma lista:

Dado a lista cores = ["verde", "rosa"]
>>> "rosa" in cores
True
>>> if "verde" in cores:
        print(está)
está

Concatenação de listas:
>>> [1,2] + [3,4]
[1,2,3,4]
Diferença entre append e concatenação!!
append = altera uma lista existente
concatenação = gera uma nova lista

Repetição de listas:
a_triplicado = a*3, sendo a [1,2,3]
[1,2,3,1,2,3,1,2,3] valores de a repetidos 3 vezes.

Remoção de elementos em listas:
a = [1,2,3]
del 2
>>> a
[1,3]
Outro exemplo:
teste = [1,2,3,4,5,6,7,8]
del teste[:6]
>>> teste
[7,8]

Ordenação de lista:
lista.sort() ou sorted(lista)
lista.sort():
Ordena a propria lista, sem criar uma nova
'''py
lista = [3, 1, 2]
lista.sort()
print(lista)  # Saída: [1, 2, 3]
'''
sorted(lista):
Cria uma nova lista sem alterar a original
'''py
lista = [3, 1, 2]
nova_lista = sorted(lista)
print(lista)      # Saída: [3, 1, 2]
print(nova_lista) # Saída: [1, 2, 3]
'''

"""
