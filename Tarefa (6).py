#Leia um valor em metros e o exiba convertido em centimetros e milimetros

num=float(input('Digite um valor em metros, para converter: '))

cem=num*100
mili=num*1000

print('\nConvertendo {}...'.format(num))
print('\nEm centimetros: {} \nEm milimetros: {}'.format(cem, mili))