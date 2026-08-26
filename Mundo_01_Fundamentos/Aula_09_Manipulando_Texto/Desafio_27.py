'''
Criar um programa que leia o nome completo de
uma pessoa e mostre separadamente o primeiro e
o último nome.
'''

nome_completo = str(input('Digite o seu nome completo: '))
primeiro_nome = nome_completo.split()[0]
ultimo_nome = nome_completo.split()[-1]
print(f'O seu primeiro nome é {primeiro_nome}')
print(f'O seu úlimo nome é {ultimo_nome}')
