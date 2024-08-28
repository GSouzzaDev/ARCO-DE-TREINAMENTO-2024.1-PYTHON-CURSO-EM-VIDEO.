#Escreva um programa que pergunte a quantidade de Km
#percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preco a se pagar, sabendo que o carro
#custa RS60 por dia e 0,15 por km rodado

km=float(input('KMs andados:'))
dias=int(input('Digite os dias de aluguel'))

apagar=km*0.15+dias*60

print(f'Preco a ser pago: {apagar}')