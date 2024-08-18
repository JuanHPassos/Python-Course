#Função principal - define o modo do jogo(Inicio do jogo)
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    #Variavel usada para selecionar o modo do jogo.
    modo_de_jogo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    if modo_de_jogo == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()
    else:
        print("\nVoce escolheu um campeonato!\n")
        campeonato()

#Função campeonato - executa 3 partidas e exibi rodadas e placar, alem de indicar o fim
def campeonato():
    #Pontos computador
    computador = 0
    #Pontos jogador
    jogador = 0
    #i começa em 1 e vai ate 3, definindo as 3 rodadas
    for i in range(1,4):
        print(f"\n**** Rodada {i} ****\n")
        vencedor = partida()
        if vencedor:
            computador = computador + 1
        else:
            jogador = jogador + 1
    
    print("\n**** Final do campeonato! ****")
    print(f"\nPlacar: Você {jogador} X {computador} Computador")
#Função partida - le n e m, define quem começa, chama as funções de jogadas e exibi o vencedor   
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    #Variavel que define o turno do jogador, se valer 0, o computador joga, e 1 o usuario joga.
    turno = 0
    #Se n for multiplo de m+1, o usuario começa
    if not n%(m+1):
        print("\nVocê começa!")
        turno = 1
    #Senao
    else:
        print("\nComputador começa!\n")
    #Enquanto houver peças no tabuleiro
    while(n):
        #Turno usuario
        if turno:
            #Valor atual de peças é igual a n - as peças tiradas
            n = n - usuario_escolhe_jogada(n,m)
        #Turno computador
        else:
             #Valor atual de peças é igual a n - as peças tiradas
            n = n - computador_escolhe_jogada(n,m)
        #Troca de turno
        turno = not turno
        #Se o jogo nao tiver acabado
        if n != 0:
            #Mensagem especifica para apenas uma peça
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            #Restam n peças
            else:
                print(f"Agora restam {n} peças no tabuleiro.")
    #O ganhador é o do turno passado, logo se turno = 1, o computador venceu.
    if turno:
        print("Fim do jogo! O computador ganhou!")
    #Se for igual a 0, vitoria do usuario.
    else:
        print("Fim do jogo! Você ganhou!")
    #Retorno que define o vencedor da rodada(1 = computador, 0 = jogador)
    return turno    
        
def usuario_escolhe_jogada(n,m):
    #Variavel que prende o usuario até digitar uma entrada válida
    x = -1
    #Enquanto a entrada nao for valida
    while x < 1 or x > m:
        #Se a primeira entrada for invalida, então a cada entrada invalida, o usuario é notificado
        if x != -1: print("\nOops! Jogada inválida! Tente de novo.")
        
        x = int(input("\nQuantas peças você vai tirar? "))
    if x == 1:
        print("\nVocê tirou uma peça.")
    else:
        print(f"Você tirou {x} peças.")
    #Retorna-se o valor de peças tiradas
    return x
    
def computador_escolhe_jogada(n, m):    
    #Começa-se o i em m, para retirar o maximo de peças possiveis, dessa forma, o jogo fica mais dinamico.
    #nota: range(inicio, para n+1(-1+1 = 0), i = i + atualição)
    for i in range(m, -1, -1):
        #Estrategia para o computador vencer.
        if not ((n-i)%(m+1)):
            #Se achou, não ha mais necessidade de procurar 
            break
    #Mensagem especificada para uma peça
    if(i ==1):
        print("\nO computador tirou uma peça.")
    else:
        #Se o for nao encontrou nenhum numero, retira-se m peças, como especifcado pelo problema
        if(i == 0):
            i = m
        print(f"\nO computador tirou {i} peças.")
    return i
#Este bloco verifica se o script está sendo executado diretamente (ou seja, não está sendo importado como um módulo em outro script). Se estiver, a função main() é chamada.
if __name__ == "__main__":
    main()
