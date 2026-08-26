'''
Criar um programa que leia o nome de uma pessoa
e diga se ela tem 'Silva' no nome (em qualquer posição).
'''

nome = str(input('Digite o seu nome: '))
nome_formatado = nome.lower()
print('silva' in nome_formatado)

