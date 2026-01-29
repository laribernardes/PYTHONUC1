n1 = int (input('Digite 1 número: '))
n2 = int (input('Digite 1 número: '))
n3 = int (input('Digite 1 número: '))
n4 = int (input('Digite 1 número: '))
n5 = int (input('Digite 1 número: '))
nu = [n1, n2, n3, n4, n5]

def soma_elementos ():
    vetor= [nu]

soma = sum(nu)
print(f'A soma de {nu} é: {soma}')

if __name__ == '__main__' :
    soma_elementos ()