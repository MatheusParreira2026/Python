'''
Criar um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados
(unidade, dezena, centena e milhar).
'''

numero = int(input('Digite um número: '))
unidade = (numero // 1) % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10
print(f'A unidade do número {numero} é igual a {unidade}')
print(f'A dezena do número {numero} é igual a {dezena}')
print(f'A centena do número {numero} é igual a {centena}')
print(f'A milhar do número {numero} é igual a {milhar}')