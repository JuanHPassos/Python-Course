import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    #Formula-> S = somatorio da subtração dos iesimos elemento de as_a e as_b dividida por 6 -> S = abs(as_a[i]-as_b[i])/6, sendo i de 0 a 5.
    #Grau de similariedade entre o texto "a" e "b"
    S = 0
    #Percorrer os elementos da posição 0 a 5.
    for i in range(6):
        S = S + abs(as_a[i]-as_b[i])
    #Dividir o somatorio por 6.
    S = S/6
    #Retorna grau de similaridade.
    return S

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    quant_palavras_unicas = 0
    quant_palavras_diferentes = 0
    n_total_palavras = 0
    sum_wordsize = 0
    n_total_frases = 0
    n_carac_sentenca = 0
    n_carac_frase = 0
    #Sentencas recebe uma lista com as sentencas do texto.
    sentencas = separa_sentencas(texto)
    #Lista para guardar listas das frases.
    lista_lista_frases = []
    #Percorrer todas as sentencas.
    for sentenca in sentencas:
        #Calcular o numero de caracteres de todas as sentencas.
        n_carac_sentenca = n_carac_sentenca + len(sentenca)
        #Adicionar lista de frases a uma lista.
        lista_lista_frases.append(separa_frases(sentenca))
    #Lista que guarda listas de palavras.
    lista_lista_palavras = []
    #Percorrer todas as listas de frase.
    for lista_frases in lista_lista_frases:
        #Calcular o numero total de frases do texto.
        n_total_frases = n_total_frases + len(lista_frases)
        #Percorrer todas as frases da lista.
        for frase in lista_frases:
            #Guardar numero de caracteres que formam todas as frases.
            n_carac_frase = n_carac_frase + len(frase)
            #Adciona uma lista de palavras a lista.
            lista_lista_palavras.append(separa_palavras(frase))
    #Lista para guardar todas as palavras.
    todas_palavras = []
    #Percorrer todas as listas de palavras.
    for lista_palavras in lista_lista_palavras:
        #Guardar a quantidade de todas as palavras do texto.
        n_total_palavras = n_total_palavras + len(lista_palavras)
        #Concatenação de listas(objetivo:lista com todas as palavras).
        todas_palavras = todas_palavras + lista_palavras
        #Percorrer todas as palavras do texto.
        for palavra in lista_palavras:
            #Guardar a soma do tamanho de todas as palavras.
            sum_wordsize = sum_wordsize + len(palavra)
    #Acha o numero de palavras diferentes em todo o texto.     
    quant_palavras_diferentes = n_palavras_diferentes(todas_palavras)
    #Acha o numero de todas as palavras unicas em todo o texto.
    quant_palavras_unicas = n_palavras_unicas(todas_palavras)
    #Tamanho medio de palavra.
    wal = sum_wordsize/n_total_palavras
    #Relação Type-Token.
    ttr = quant_palavras_diferentes/n_total_palavras
    #Razão Hapax Legomana.
    hlr = quant_palavras_unicas/n_total_palavras
    #Tamanho médio de sentença.
    sal = n_carac_sentenca/len(sentencas)
    #Complexidade de sentença.
    sac = n_total_frases/len(sentencas)
    #Tamanho médio de frase.
    pal = n_carac_frase/n_total_frases
    #Retorna a assinatura do texto.
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    #Variavel que indica o numero do texto atual.(começa no dois, pois o primeiro é analisado antes do for)
    indice = 2
    #Numero do texto com maior probabilidade.(inicia em um porque o texto 1 é analisado antes do for)
    numero = 1
    #Começar o calculo de assinatura antes do for para inicializar a variavel menor_grau.
    as_a = calcula_assinatura(textos[0])
    menor_grau = compara_assinatura(as_a, ass_cp)
    #Percorrer todos os textor a partir do segundo.
    for texto in textos[1:]:
        #Calculo assinatura do texto.
        as_a = calcula_assinatura(texto)
        #Guardar o grau em uma variavel auxiliar.
        auxiliar = compara_assinatura(as_a, ass_cp)
        #Se o grau for menor, seu valor é salvado e guarda-se o indice.
        if(menor_grau > auxiliar):
            menor_grau = auxiliar
            numero = indice
        #Atualiza o indice para o proximo texto.
        indice = indice + 1
    #Retorna-se o numero do texto com mais probalidade de ser copia.
    return numero
#Funcao principal - chama as funções.
def main():
    #Guarda a assinatura de comparação.
    ass_cp = le_assinatura()
    #Lista que guarda os textos a serem avaliados.
    textos = le_textos()
    #Guarda numero do texto que foi escrito por um aluno infectado por COH-PIAH.
    texto_COHPIAH = avalia_textos(textos, ass_cp)
    #Saida esperada.
    print(f"O autor do texto {texto_COHPIAH} está infectado com COH-PIAH")

#Inicio do programa apos o interpretador conhecer as funções.    
main()
