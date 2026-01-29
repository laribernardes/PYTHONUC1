num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

if contador == 2:
    print("Número primo")
else:
    print("Não é primo")
