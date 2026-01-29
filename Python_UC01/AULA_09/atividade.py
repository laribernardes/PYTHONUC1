vetor_dados=[10, 20, 30, 40, 50, 76, 43, 90, 13, 21]
vetor_dados_2=[10, 20, 30, 40, 50]


def exemplo_1 ():
    vetor = [10, 20, 30, 40, 50]
    print(f"Vetor: {vetor}")

def exemplo_1_1 (vetor):    
    print(f"Vetor: {vetor}")

def exemplo_2 (vetor) :
    for elemento in vetor:
        print("Elemento:", elemento)

def soma():
 soma = sum( vetor_dados_2)
 print (f'A soma dos elementos é', soma ) 

if __name__ == "__main__" :
    #exemplo_1 ()
    #exemplo_1_1 (vetor_dados)
    #exemplo_1_1 (vetor_dados_2)

    #exemplo_2 (vetor_dados)
     soma()