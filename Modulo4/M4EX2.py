#Imprima os n primeros numeros primos
n = int(input("Digite o valor de n: "))
impar = 1
while n:
    if impar%2:
        print(impar)
        n = n-1
    impar = impar + 2
    