#Par ou Ímpar e Positivo ou Negativo?#

numero = int(input('Digite um número: '));

if numero % 2 == 0:
    print('O número é par!')

else:
    print('Onúmero é impar!')


if numero > 0:
    print('O número é positivo!')

elif numero < 0:
    print('Onúmero é negativo!')

else:
    print('O número é zero!')