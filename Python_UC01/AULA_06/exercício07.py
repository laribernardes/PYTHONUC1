#Calcular o fatorial de um número usando while#

num = int(input("Digite um número: "))
fatorial = 1

while num > 1:
    fatorial *= num
    num -= 1

print(fatorial)
