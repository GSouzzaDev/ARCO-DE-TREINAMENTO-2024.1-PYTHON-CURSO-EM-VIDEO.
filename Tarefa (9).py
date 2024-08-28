#Faça um programa que leia a largura e a altura de uma parede em
#metros, calcule a sua area e a quantidade de tinta necessaria para
#pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m2

print('Vamos determinar a quantidade de tinta necessaria para pintar sua parede!')

largura=float(input('Digite a largura'))
altura=float(input('Digite a altura'))

M2=largura*altura

print(f'Sua parede tem {M2} metros quadrados')
print(f'Voce precisara de {M2/2} litros de tinta')