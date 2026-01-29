matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
]

matriz_4_4 = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
   [13, 14, 15, 16]
   
]

#def matrizes():
print('Elemento (0,0):', matriz[0][0])  #Saída: 1
print('Elemento (2,1):', matriz[2][1])  #Saída: 8

def linha_matriz():
 for linha in matriz:
     print (f'|', end = ' ')
     for elemento in linha:
        print(elemento, end = ' | ')
     print() 

def exibindo_matriz():

  for linha in matriz:
    print(linha)

matriz = []
for i in range(4):
   linha = []
   for j in range(4):
      valor = int(input(f'Digite o valor para [{i}] [{j}]: '))
      linha.append(linha)

for linha in matriz:
   print(linha)


def soma_elementos_secundarios():
  soma = 0 
  for i in range(4):
     soma = soma + sum(matriz_4_4 [i])

 
def maior_valor():
 for i in range(4):
     maior = matriz [i][0]
 for j in range(4):
         if matriz[i][j] > maior:
          maior = matriz[i][j]
print(f'Maior valor da linha {i}: {maior}')

def numeros_pares():
 pares = 0 
 for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares = pares + 1
        
print(f'Quantidade de números pare: {pares}')

def multiplicaçao_linhas_numeros():
     
 num = int(input("Digite o número para multiplicação: "))
 linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

 for j in range(4):
    matriz[linha_escolhida][j] *= num

    for linha in matriz:
        print(linha)