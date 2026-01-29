compra = float(input('Digite o valor de sua compra para que o desconto possa ser aplicado: '));

if compra > 500:
    desconto = 0.15

elif compra > 200 and compra < 500:
    desconto = 0.10

elif compra < 200:
    desconto = 0.05

valor_final = compra - (compra * desconto)

print(f'Desconto aplicado: {desconto* 100:.0f}%')
print(f'Valor final da compra {valor_final:.2f}')