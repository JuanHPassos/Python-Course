#Calcule a soma dos algarismos de n
n = int(input(""))
soma = 0
while n:
    soma = soma+(n%10)
    n = n//10
print(soma)