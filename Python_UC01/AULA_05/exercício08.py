idade = int(input('Digite sua idade: '));
carteira = input('Tem carteira de motorista?(s/n): ');

if idade >= 18 and carteira == 's':
    print('Você pode dirigir!')

else:
    print('Você não pod dirigir!')