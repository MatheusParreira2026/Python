'''
Faça um algoritmo qeu leia o preço de um produto
e mostre o seu novo preço com 5% de desconto.
'''

preco = float(input('Digite o preço do seu produto: R$ '))
novo_preco = preco * 0.95
print(f'O preço do produto com um desconto de 5% é igual a: R$ {novo_preco:.2f}')

'''
Alternativa
'''

preco = float(input('Digite o preço do seu produto: R$ '))
novo_preco = preco - (preco * 5 / 100)
print(f'O preço do produto com um desconto de 5% é igual a: R$ {novo_preco:.2f}')