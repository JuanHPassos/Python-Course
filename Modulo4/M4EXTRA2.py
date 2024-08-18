#Se n possuir dois numeros iguais juntos, imprima "sim", senão, "não"
n = int(input(""))
#aux recebe o numero das unidades de n
aux = n%10
#apaga-se o numero de unidade de n
n = n//10
while n:
    #Como aux e n%10, sao sempre adjcentes, se eles forem iguais, imprimi-se "sim"
    if(aux == n%10):
        print("sim")
        aux = -1
        #Encerra-se as comparações
        break
    aux = n%10
    n = n//10
if(aux != -1):
    print("não") 