#Controle de Entrada em uma Festa#

idade = int(input('Digite sua idade: '));
p = input('Está acompanhado(a) dos seus pais?: ');

if idade >= 18:
    print('Acesso permitido!')

elif (idade < 18) and ( p == 'sim'):
    print('Acesso permitido!')

else:
    print('Acesso negado!')