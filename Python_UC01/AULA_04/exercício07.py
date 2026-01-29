peso = float(input('Digite seu peso: '));
altura = float(input('Digite a sua altura: '));

imc = peso / (altura**2)

if imc < 18.5:
    print(f'Seu IMC é: {imc:.1f},você está a baixo do peso');

elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC é: {imc:.1f},você está com o peso ideal!');

elif imc >= 30.0:
    print(f'Seu IMC é: {imc:.1f},você está com sobrepeso!');
