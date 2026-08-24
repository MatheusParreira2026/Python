'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
O desafio consiste em criar um programa que ajude o professor lendo o nome
dos quatro alunos e exibindo na tela o nome do aluno escolhido para a tarefa.

DICA: O aluno deve utilizar funcionalidades presentes nos módulos (bibliotecas)
do Python. Específicamente, ele sugere buscar um módulo que lide com números aleatórios
ou seleções randômicas, permitindo que o computador faça a escolha entre os nomes fornecidos.
'''

from random import choice

nome_01 = input('Digite o primeiro nome: ')
nome_02 = input('Digite o segundo nome: ')
nome_03 = input('Digite o terceiro nome: ')
nome_04 = input('Digite o quarto nome: ')

nomes =[nome_01, nome_02, nome_03, nome_04]
nome_escolhido = choice(nomes)

print(f'O aluno escolhido para a tarefa é: {nome_escolhido}')