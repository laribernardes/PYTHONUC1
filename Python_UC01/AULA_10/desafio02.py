matriz = [ 
    [1,2],
    [3,4]

]

matriz_2 = [
    [5,6],
    [7,8]
]


def soma_matrizes():
    soma = 0
    for i in range(4):
     soma = sum( matriz, [matriz_2])

    print(f'A soma das matrizes é: {soma}')

if __name__ == '__main__':
        soma_matrizes()