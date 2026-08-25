'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente.

DICA: O aluno deve carregar o módulo matemático apropriado para realizar os
cálculos trigonométricos de forma simples.
'''

from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo:'))

conversor_seno = sin(radians(angulo))
conversor_cosseno = cos(radians(angulo))
conversos_tangente = tan(radians(angulo))

print(f'Valor do seno: {conversor_seno:.2f}')
print(f'Valor do cosseno: {conversor_cosseno:.2f}')
print(f'Valor da tangente: {conversos_tangente:.2f}')
