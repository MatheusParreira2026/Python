'''
Escreva um programa onde o computador "pensa" em um número inteiro
entre 0 e 5. O objetivo do programa é pedir para o usuário tentar
adivinhar qual foi o número escolhido pelo computador e, em seguida,
informar na tela se o usuário venceu ou perdeu.
'''

from random import randint

numero_escolhido = int(input('Digite um número inteiro entre 0 e 5: '))

if numero_escolhido in range(0, 6):
    numero_sorteado = randint(0, 5)
    if numero_escolhido == numero_sorteado:
        print(f'Parabens! O número {numero_escolhido} é igual ao número sorteado {numero_sorteado}!')
    else:
        print(f'Que pena. O número escolhido {numero_escolhido} é diferente do número sorteado {numero_sorteado}')
else:
    print('Opção inválida. Escolha um número entre 0 e 5')
