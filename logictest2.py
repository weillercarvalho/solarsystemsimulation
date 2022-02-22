#Lógica de Programação
'''
numero = int(input('Digite um número:'))

acerto = False
while acerto == False:
  if numero < 0:
    print ('Número inválido')
    numero = int(input('Digite um número:'))
  else:
   acerto = True
   fatorial = 1
   for num in range(1,numero +1):
    fatorial = fatorial * num
    print(fatorial)
'''
'''
n=-37
bin(n)
print(bin(n))
print(n.bit_length())
'''
'''
idade=32
salario=4590.9
nome='Maria Silva'
sexo='F'
print(f"A funcionária {nome}, do sexo {sexo} tem o salario de {salario:.2f} e a idade de {idade} anos")
'''
"""
idade=32
salario=4590.9
nome='Maria Silva'
sexo='F'
print('A funcionaria {:s}, do sexo {:s} tem o salário de {:.2f} e a idade de {:d} anos'.format(nome, sexo, salario, idade))
"""
'''
soma=1
x=int(input('Digite um número'))
while x != 0:
    soma=x-soma
    print("SOMA = ", soma)
'''

'''
nome=int(input('Digite um numero'))
soma=0
for i in range(0,nome+1):
    soma=soma+i
    print('Soma=',soma)

    '''
'''
raio=int(input('Digite o raio:'))
pi=3.141516
C= 2* pi * raio
print('C é:', C)
'''
'''
n=int(input('Digite o número de letras da palavra'))
if n>1:
  p=n-1
  a=p*n
  print('Numero de combinações é:', a)
else:
  print('Valor invalido')
'''
'''
frutas=['Limao', 'Laranja']
frutas_redondas=frutas.copy()
print(frutas_redondas)
'''
#Vetor
'''
N=int(input('Digite a quantidade de números:'))
vet=([0 for x in range(N)])
for i in range(0,N):
  vet[i]=float(input('Digite um número'))
  print()
  print('Número digitados:')
for i in range(0,N):
  print(f"{vet[i]:.1f}")
'''
#Matrizes

'''
M=int(input('Digite o número de linhas da matriz:'))
N=int(input('Digite o número de colunas da matriz:'))
mat=[[0 for x in range (N)] for x in range(M)]
for i in range(0,M):
  for j in range(0,N):
    mat[i][j] = int(input(f"Elementos[{i},{j}]: "))
print()
print('MATRIZ DIGITADA:')
for i in range(0,M):
  for j in range(0,N):
    print(f"{mat[i][j]} ", end="")
  print()

'''

















































