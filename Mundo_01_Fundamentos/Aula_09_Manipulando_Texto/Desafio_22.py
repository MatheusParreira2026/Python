'''
Criar um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiúsculas, todas as letras minúsculas,
quantas letras ao todo (sem considerar espaços) e quantas letras
tem o primeiro nome.
'''

nome = str(input('Digite o seu nome completo: '))
print(f'Em letras maiúsculas: {nome.upper()}')
print(f'Em letras minúsculas: {nome.lower()}')
print(f"Total de letras: {len(nome.strip().replace(' ', ''))}")
print(f'Total de letras do primeiro nome: {len(nome.split()[0])}')
