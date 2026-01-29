#Desconto em Compras#

produto = int(input('Digite quantos produtos você comprou: '));
valor = float(input('Digite o valor da sua compra: '));
cupom = input('Digite se você usou cupom na sua ultima compra: ');

if (produto >= 5 or valor >= 100) and cupom == 'não':
    print('Desconto recebido!')

else:
    print('Desconto negado!')

