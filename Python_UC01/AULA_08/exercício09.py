def fatorial(n):
    if n < o:
        return 'Numeros inválidos para fatorial.'
    elif n == 0:
        return 1 
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
    def testar_fatorial () :
        
        # Exemplo de chamada
        numero = int(input('informe um número:'))
        resultado = fatorial(numero)
        print(f'\n\n\tFatorial de {numero} é igual á {resultado}\n\n')
        #print(f'Fatorial de 5:', fatorial(5))

    if __name__ == '__main__':

        #resultado=soma(sys.argv[1:])
        #pritn (f'O valor da soma dos números é {resultado})

        #testar_soma

        testar_fatorial()
