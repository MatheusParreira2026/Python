'''
Criar um programa que leia uma frase e mostre:
quantas vezes aparece a letra 'A', em que posição
ela aparece a primeira vez e em que posição ela
aparece a última vez.
'''

frase = str(input("Digite uma frase: "))
print(f'A letra A aparece {frase.lower().count('a')} vezes.')
print(f'A posição que a letra A aparece pela primeira vez: {frase.lower().find('a')}')
print(f'A posição que a letra A aparece pela última vez: {frase.lower().rfind('a')}')
