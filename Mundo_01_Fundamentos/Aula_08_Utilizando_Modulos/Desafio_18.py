'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente.

DICA: O aluno deve carregar o módulo matemático apropriado para realizar os
cálculos trigonométricos de forma simples.
'''

import math

seno = float(input('Digite o valor do ângulo seno:'))
cosseno = float(input('Digite o valor do ângulo cosseno: '))
tangente = float(input('Digite o valor do ângulo tangente: '))

conversor_seno = math.radians(seno)
conversor_cosseno = math.radians(cosseno)
conversos_tangente = math.radians(tangente)

seno_resultado_final = math.sin(conversor_seno)
cosseno_resultado_final= math.cos(conversor_cosseno)
tangente_resultado_final = math.tan(conversos_tangente)

print(f'Valor do seno: {seno_resultado_final:.4f}')
print(f'Valor do cosseno: {cosseno_resultado_final:.4f}')
print(f'Valor da tangente: {tangente_resultado_final:.4f}')
