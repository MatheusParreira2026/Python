'''
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar.
Considere US$1,00 = R$3,27
'''

real =  float(input('Digite o valor total do seu dinheiro em reais: '))
conversor = real * 3.27
print(f'R${real:.2f} convertido em dólares é igual a: US${conversor:.2f}')

