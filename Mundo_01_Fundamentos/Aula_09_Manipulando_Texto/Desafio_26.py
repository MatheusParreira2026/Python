'''
Criar um programa que leia uma frase e mostre:
quantas vezes aparece a letra 'A', em que posição
ela aparece a primeira vez e em que posição ela
aparece a última vez.
'''

# frase = str(input("Digite uma frase: "))
# print(f'A letra A aparece {frase.lower().count('a')} vezes.')
# print(f'A posição que a letra A aparece pela primeira vez: {frase.lower().find('a')}')
# print(f'A posição que a letra A aparece pela última vez: {frase.lower().rfind('a')}')

'''
Alternativa correta

Pontos principais explicados pelo professor:

.strip(): Remove os espaços inúteis no início e no fim da 
frase para não atrapalhar a contagem das posições (7:38).

.upper(): Converte a string para maiúsculas, garantindo que o programa 
conte tanto 'A' quanto 'a' (4:06).

.count('A'): Conta quantas vezes a letra aparece (3:05).

.find('A'): Localiza a primeira ocorrência (5:03). Como o Python começa a contar
 do zero, o professor adiciona + 1 para exibir a posição correta para o usuário (5:34).
 
.rfind('A'): Localiza a última ocorrência (o 'r' vem de right, procurando da direita para a esquerda) (6:11).
'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))