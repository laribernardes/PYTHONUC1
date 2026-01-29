#Soma de números positivos#

soma = 0
numero = 0

while numero >= 0:
    numero = int(input("Digite um número: "))

    if numero >= 0:
        soma += numero

print("Soma dos números positivos:", soma)
