#Juros simples#

capital = float(input('Digite o valor inicial: '));
taxa = float(input('Digite a taxa de juros (% ao mês:): '));
tempo = int(input('Digite o tempo (em meses): '));

taxa = taxa / 100

montante = capital * (1 + taxa * tempo);

print(f'Montante final: R$ {montante:.2f}');
