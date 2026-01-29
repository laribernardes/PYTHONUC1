maior = int(input("Digite um número: "))

for i in range(4):
    num = int(input("Digite outro número: "))
    if num > maior:
        maior = num

print("Maior número:", maior)
