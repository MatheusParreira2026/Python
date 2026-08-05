'''
Crie um algoritmo que leia um número e mostre
o seu dobro tripo e raiz quadrada.
'''

# n = int(input("Digite um número: "))
# print(f'O dobro de {n} é {n*n}\nO triplo de {n} é {n*n*n}\nA raiz quadrada de {n} é {n**n}')

'''
Alternativa 01
'''

# n = int(input("Digite um número: "))
# d = n * 2
# t = n * 3
# r = n ** (1/2)
# print('O dobro de {} vale {}'.format(n, d))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

'''
Alternativa 02
'''

n = int(input("Digite um número: "))

print('O dobro de {} vale {}'.format(n, (n *2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n * 3), n, pow(n, (1/2))))
