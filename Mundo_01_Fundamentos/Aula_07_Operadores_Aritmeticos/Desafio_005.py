'''
Faça um programa que leia um
número inteiro e mostre na tela
o seu sucessor e seu antecessor.
'''

n = int(input('Digite um número inteiro: '))
print(f'O número sucessor a {n} é {n+1}\nO número antecessor a {n} é {n-1}')

'''
Alternativo
'''

n = int(input('Digite um número inteiro: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(n, a, s))