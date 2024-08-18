#Calculo fatorial de n
n = int(input("Digite o valor de n: "))
ans = 1
while n:
    ans = ans*n
    n = n-1
print(ans)
