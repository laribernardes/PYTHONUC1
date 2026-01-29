#Cadastro de Usuário#

nome = input('Digite seu nome: ');
senha = input('Digite sua senha: ');

if len(nome) >= 3 and len(senha) >= 6 and senha != '123456' and senha != 'senha':
    print('Cadastro permitido!')

else:
    print('cadastro negado!')