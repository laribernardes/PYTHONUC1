idade = int(input('Digite a sua idade: '));
autorizacao = input('Você tem a autorização de seus pais?: ');

if idade >= 18:
    print('Você pode viajar sozinho!')

elif idade > 16 < 17 or autorizacao == 'sim':
    print('Você pode viajar sozinho!');

else:
    print('Você não pode viajar sozinho!')