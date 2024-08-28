#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
#dolares ela pode comprar
#1 dolar = 5,51 em 28/08/24

real=float(input('Digite quanto tem na sua carteira: '))

print(f'Com {real} reais, voce pode comprar {real/5.51:.2f} dolares!')