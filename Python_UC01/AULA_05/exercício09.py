#Login no Sistema 🔐#

usuario = input('Digite o nome de usuário:');
senha = int(input('Digite a senha: '));

if usuario == 'admin' and senha == 1234:
    print('Acesso permitido!')

else:
    print('Acesso negado!')