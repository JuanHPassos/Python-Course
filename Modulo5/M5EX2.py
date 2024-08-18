#Função que retorna o primeiro primo menor ou igual a n
def maior_primo(n):
    while(n):
        primo = 1
        for i in range(2,int(n/2)+1):
            if(not n%i):
                primo = 0
                break
        if primo:
            return n
        else:
            n = n - 1
