#Imprimir "primo" se n for primo, caso contrario, imprima "não primo"
import math
n = int(input("Digite um número inteiro: "))
primo = 1
#i começa em 2 e termina n//2
for i in range(2, n//2+1):
    #Se for divisivel por algum numero, não é primo
    if(n%i == 0):
        primo = 0
        break
#Se primo == 1, n não é divisivel por nenhum numero de 2 até sua metade, logo, ele é primo
if(primo): 
    print("primo")
else:
    print("não primo")
