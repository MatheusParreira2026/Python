'''
Criar um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiúsculas, todas as letras minúsculas,
quantas letras ao todo (sem considerar espaços) e quantas letras
tem o primeiro nome.
'''

# nome = str(input('Digite o seu nome completo: '))
# print(f'Em letras maiúsculas: {nome.upper()}')
# print(f'Em letras minúsculas: {nome.lower()}')
# print(f"Total de letras: {len(nome.strip().replace(' ', ''))}")
# print(f'Total de letras do primeiro nome: {len(nome.split()[0])}')

'''
Alternativa 01
Para resolver este desafio, o professor Gustavo Guanabara utiliza 
métodos de manipulação de strings em Python. O código abaixo utiliza
a abordagem que separa os nomes em uma lista para facilitar a contagem
do primeiro nome.
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
