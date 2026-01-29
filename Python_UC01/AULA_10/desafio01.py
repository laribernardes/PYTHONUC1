matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for linha in matriz:
     print (f'|', end = ' ')
     for elemento in linha:
        print(elemento, end = ' | ')
     print() 
if __name__ == '__main__':
  print() 