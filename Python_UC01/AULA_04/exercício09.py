t = input('Digite a temperatura (em Celsius): ');

if t <= '0°C':
    print('Está muito frio')

elif t >= '1°C' and t < '20°C':
    print('Está um clima agradável!')

elif t > '20°C':
    print('Está fazendo um calorão!')