'''
Desafio 45 (25:13): Crie um programa que faça o computador jogar Jokenpô (pedra, papel e tesoura) com você.
'''

# from random import choice
#
# cores = {
#     # Reset
#     'limpa': '\033[m',
#
#     # Cores normais
#     'preto': '\033[30m',
#     'vermelho': '\033[31m',
#     'verde': '\033[32m',
#     'amarelo': '\033[33m',
#     'azul': '\033[34m',
#     'magenta': '\033[35m',
#     'ciano': '\033[36m',
#     'branco': '\033[37m',
#
#     # Cores claras / brilhantes
#     'cinza': '\033[90m',
#     'vermelhoclaro': '\033[91m',
#     'verdeclaro': '\033[92m',
#     'amareloclaro': '\033[93m',
#     'azulclaro': '\033[94m',
#     'magentaclaro': '\033[95m',
#     'cianoclaro': '\033[96m',
#     'brancoclaro': '\033[97m',
#
#     # Estilos
#     'negrito': '\033[1m',
#     'fraco': '\033[2m',
#     'sublinhado': '\033[4m',
#     'piscando': '\033[5m',
#     'invertido': '\033[7m',
#
#     # Combinações
#     'pretoebranco': '\033[7;97m',
# }
#
# print("Escreva PEDRA, PAPEL ou TESOURA.")
#
# jogador = str(input("Escreva uma das opções acima: ")).strip().upper()
#
# escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
# computador = choice(escolhas)
#
# if jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'TESOURA' and computador == 'PAPEL':
#     print(f"{cores['verde']}Você escolheu {jogador} e o computador escolheu {computador}! Sendo assim você VENCEU!{cores['limpa']}")
# elif jogador == 'PEDRA' and computador == 'PAPEL' or jogador == 'PAPEL' and computador == 'TESOURA' or jogador == 'TESOURA' and computador == 'PEDRA':
#     print(f"{cores['vermelho']}Você escolheu {jogador} e o computador escolheu {computador}! Sendo assim você PERDEU!{cores['limpa']}")
# elif jogador == computador:
#     print(f"{cores['amarelo']}Você escolheu {jogador} e o computador também escolheu {computador}! Sendo assim EMPATOU!{cores['limpa']}")
# elif jogador != escolhas:
#     print(f"{cores['azul']}Você escreveu {jogador}. Essa palavra não é válida, tente novamente.{cores['azul']}")

'''
Alternativa feita pelo professor
'''
from random import randint
from time import sleep

# Define as opções disponíveis em uma tupla
itens = ('Pedra', 'Papel', 'Tesoura')

# Computador escolhe uma opção aleatória entre 0 e 2
computador = randint(0, 2)

# Menu do jogador
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

# Efeito dramático do Jokenpô
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

# Validação do resultado do jogo
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
