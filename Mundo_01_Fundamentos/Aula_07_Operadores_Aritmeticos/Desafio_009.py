'''
Faça um programa que leia um número inteiro qualquer
e mostre na tela sua tabuada.
'''

# n = int(input('Digite um número inteiro: '))
#
# n1 = n * 1
# n2 = n * 2
# n3 = n * 3
# n4 = n * 4
# n5 = n * 5
# n6 = n * 6
# n7 = n * 7
# n8 = n * 8
# n9 = n * 9
# n10 = n * 10
#
# print(f'>>>TABUADA DO NÚMERO {n}<<<')
# print(f'{n} x 1 = {n1}')
# print(f'{n} x 2 = {n2}')
# print(f'{n} x 3 = {n3}')
# print(f'{n} x 4 = {n4}')
# print(f'{n} x 5 = {n5}')
# print(f'{n} x 6 = {n6}')
# print(f'{n} x 7 = {n7}')
# print(f'{n} x 8 = {n8}')
# print(f'{n} x 9 = {n9}')
# print(f'{n} x 10 = {n10}')

'''
Alternativa
'''

num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 20)
print('{} x {:2} = {}'.format(num, 1, num * 1))
print('{} x {:2} = {}'.format(num, 2, num * 2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {:2} = {}'.format(num, 10, num * 10))
print('-' * 20)