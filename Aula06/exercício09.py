#Tabela de multiplicação de um número (de 1 a 10)#

num = int(input("Digite um número: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
