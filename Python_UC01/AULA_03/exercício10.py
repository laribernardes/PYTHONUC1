#Conversor de moedas#

reais = float(input('Digite o valor em reais (R$): '));
cotacao = float(input('Digite a cotação do dólar: '));

dolares = reais / cotacao 

print(f'Valor em dolares : US$ {dolares:.2f}');