#Peça o nome do usuário, de boas vindas com seu nome.
#Peça sua data de nascimento e a ordene.
#Some dois números inteiros.
nome=input('Qual o seu nome?')
print('Bem vindo(a)', nome)

print('Digite a sua data de nascimento')
dia=input('Dia:')
mes=input('Mes:')
ano=input('ano:')

print('voce nasceu no dia', dia, 'no mes', mes, 'do ano', ano, nome)

print('por fim, vamos somar dois numeros')
n1=int(input('primeiro numero: '))
n2=int(input('segundo numero: '))
print('soma entre {} e {} resulta em {}'.format(n1,n2,n1+n2))