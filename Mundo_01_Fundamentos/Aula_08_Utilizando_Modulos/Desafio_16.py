'''
crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira.
Por exemplo, se o usuário digitar o valor 6.127, o programa deve exibir apenas o número 6.

DICA:O aluno deve examinar as funções disponíveis dentro da classe do módulo math,
que foi o módulo importado durante a aula para realizar manipulações numéricas.
'''
# import math
# numero = float(input("Digite um número: "))
# porcao_inteira = math.trunc(numero)
# print(f'A porção inteira do número {numero} é {porcao_inteira}')

'''
Alternativa 01
'''
# from math import trunc
# numero = float(input("Digite um número: "))
# print(f'A porção inteira do número {numero} é {trunc(numero)}')

'''
Alternativa 02
'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
