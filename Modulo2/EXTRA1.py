"""
Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.
Input: Digite o nome do cliente: Fulano de Tal
Digite o dia de vencimento: 9
Digite o mês de vencimento: Janeiro
Digite o valor da fatura: 350,00
Output:
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
"""
#str() = cast para string
nome = str(input("Digite o nome do clinete: "))
vencimento = str(input("Digite o dia do vencimento: "))
mes_ven = str(input("Digite o mês de vencimento: "))
fatura = str(input("Digite o valor da fatura: "))
#Utiliza-se f strings para a impressão das variaveis, para saida ser formatada corretamente.
print(f"Olá, {nome}\nA sua fatura com vencimento em {vencimento} de {mes_ven} no valor de R$ {fatura} está fechada.")
