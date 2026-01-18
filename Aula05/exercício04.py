#Jogo de Adivinhação#

numero_secreto = 7

palpite = int(input('Digite um número entre 1 e 10: '));

if palpite == numero_secreto:
        print('Parabéns você acertou!')
    
else:
    palpite = int(input('Tentativa 2 - Digete um número entre 1 e 10: '));
    if palpite == numero_secreto:
     print('Parabéns você acertou!');
    
    else:
        palpite = int(input('Tentativa 3 - Digete um número entre 1 e 10: '));
        if palpite == numero_secreto:
            print('Parabéns você acertou!');

        else:
            print(f'Você perdeu! o número era {numero_secreto}!');