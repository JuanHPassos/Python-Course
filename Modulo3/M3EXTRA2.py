"""
O programa deve receber os parâmetros a, b ,c da equação ax^2+bx+c,
respectivamente, e imprimir o resultado na saída da seguinte maneira:
Quando não houver raízes reais imprima:
esta equação não possui raízes reais
Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:
a raiz desta equação é X ou
a raiz dupla desta equação é X
onde X é o valor da raiz dupla
Quando houver duas raízes reais imprima:
as raízes da equação são X e Y
onde X e Y são os valor das raízes.
Além disso, no caso de existirem 2 raízes reais distintas, 
elas devem ser impressas em ordem crescente. 
"""
import math
a = int(input())
b = int(input())
c = int(input())

delta = (b**2)-4*a*c
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        x = (-b+ math.sqrt(delta))/2*a
        print("a raiz desta equação é ",x)
    else:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        #Swap entre x1 e x2, usando apenas 2 variaveis.
        if(x1 > x2):
            x1 = x1 + x2
            x2 = x1 - x2
            x1 = x1 - x2
        print(f"as raízes da equação são {x1} e {x2}")