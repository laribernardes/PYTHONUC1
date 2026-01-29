notas = []

for i in range(5):
    notas.append(float(input("Digite uma nota: ")))

notas.remove(min(notas))

media = sum(notas) / 4
print("Média:", media)
