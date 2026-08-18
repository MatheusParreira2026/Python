'''
Faça um algoritmo que leia o salário de um
funcionário e mosntre seu novo salário, com
15% de aumento.
'''

# salario = float(input('Digite o seu salário atual: R$ '))
# aumento = (salario * 0.15) + salario
# print(f'O seu novo salário com um aumento de 15% é: R$ {aumento:.2f}')

'''
Alternativa
'''

# salario = float(input('Digite o seu salário atual: R$ '))
# aumento = salario + (salario * 15 / 100)
# print(f'Um funcionário que recebia R$ { salario:.2F} com um aumento de 15% passa a receber R$ {aumento:.2f}')

'''
Exercício extra

Crie um programa que leia o preço de um produto e calcule dois valores distintos: um com 10% de desconto
para pagamento à vista e outro com 8% de aumento para pagamento parcelado.
'''

preco = float(input("Digite o preço do produto: R$ "))
pagamento_a_vista = preco * 0.90
pagamento_parcelado = preco * 1.08
print(f'\nO produto com o preço R$ {preco:.2f} sendo pago a vista passa a valer R$ {pagamento_a_vista:.2f}')
print(f'O produto com o preço R$ {preco:.2f} sendo pago parcelado passa a valer R$ {pagamento_parcelado:.2f}')

