import sys 

def main(args):
    for arg in args:
        print(arg)

def soma (numeros):
    somatorio = 0
    for valor in numeros:
        somatorio = somatorio + valor

    print (f'O valor da soma dos números é:{somatorio}')

if __name__ == '__main__':
    soma(sys.argv[1:])