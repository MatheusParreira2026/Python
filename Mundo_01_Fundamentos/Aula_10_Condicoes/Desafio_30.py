'''
Crie um programa que leia um número inteiro qualquer fornecido pelo usuário
e informe na tela se esse número é par ou ímpar.

Este é um exercício clássico de programação que utiliza a estrutura condicional
para verificar o resto da divisão do número por 2.
'''

numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar.')
