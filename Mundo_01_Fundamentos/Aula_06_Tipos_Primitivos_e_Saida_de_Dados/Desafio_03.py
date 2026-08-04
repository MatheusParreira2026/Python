"""
Crie um script Python que leia dois números e tente
mostra a soma entre eles.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print(f"A soma de {n1} + {n2} é igual a {soma}.")

'''
Alternativa 01
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print('A soma vale: ', soma)

'''
Alternativa 02
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
