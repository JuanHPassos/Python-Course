"""
Objetos na memoria:
Objetos são dados que são armazenados na memoria do computador formada por bytes contiguos.
Objetos e referencias:
a = "banana"
cria-se um objeto do tipo string, "a"(apontador) armazena o enreço de memoria onde esta guardada a palavra banana.
b = "banana"
cria-se uma nova variavel com um novo conteudo, porem como em python !!!strings sao imutaveis!!!, a e b apontam para o endereço da variavel banana, assim referenciam o mesmo conteudo.
Em contrapartida, listas sao mutaveis.
>>> a is b(ambas referenciam apontam o mesmo objeto?)
True
c = "maça"
>>> a is c
False
>>> a = [81,82,83]
>>> b = [81,82,83]
>>> a is b
False
a aponta para um lista, b aponta para uma lista, porem seus conteudos apontam para o mesmo valor.
>>> a == b
True

Repetições e referencias:

>>> origilist = [45,76,34,55]
>>> origilist*3
[45,76,34,55,45,76,34,55,45,76,34,55]
>>> [origilist]*3
[[45,76,34,55],[45,76,34,55],[45,76,34,55]]
Listas compostas por 3 listas
>>> newlist = [origilist]*3

>>> origilist[1] = 99
>>> origilist
[45,99,34,55]

>>> newlist
[[45,99,34,55][45,99,34,55][45,99,34,55]]
newlist é formado por tres elementos(ponteiros) que apontam para a origilist(cada um), e cada ponteiro da origilist aponta para um numero, estao se mudar um elemento da origlist, altera a newlist

"""
