'''
O mesmo professor que precisava sortear um aluno agora quer sortear a ordem de apresentação
do trabalho de quatro alunos. O desafio consiste em criar um programa que leia
o nome dos quatro alunos e mostre na tela a ordem sorteada para as apresentações.

DICA: Assim como no desafio anterior, você deve utilizar as funcionalidades do módulo
de números aleatórios (bibliotecas do Python). A dica aqui é procurar uma função dentro
desse módulo que permita embaralhar uma lista de itens, em vez de apenas selecionar um único elemento.
'''


from random import shuffle

nome_01 = input('Digite o primeiro nome: ')
nome_02 = input('Digite o segundo nome: ')
nome_03 = input('Digite o terceiro nome: ')
nome_04 = input('Digite o quarto nome: ')

nomes =[nome_01, nome_02, nome_03, nome_04]
shuffle(nomes)

print(f'A nova ordem é: {nomes}')