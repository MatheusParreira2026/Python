'''
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar.
Considere US$1,00 = R$3,27
'''
from idlelib import replace

# real =  float(input('Digite o valor total do seu dinheiro em reais: R$ '))
# conversor = real / 3.27
# print(f'R${real:.2f} convertido em dólares é igual a: US${conversor:.2f}')

'''Alternativo'''

import requests

real = float(input("Digite um valor monetário em reais: "))

resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

dados = resposta.json()

cotacao = float(dados['USDBRL']["bid"])

conversor = real / cotacao

real_formatado = f"{real:.2f}".replace(".", ",")

valor_formatado = f"{conversor:.2f}".replace(".", ",")

print(f'O valor de R$ {real_formatado} em dólares é igual a: US$ {valor_formatado}')

'''
Exemplo
'''
# dados = {
#     "USD": {
#         "nome": "Dólar",
#         "valor": "5.43"
#     }
# }
#
# '''
# Como chegar até "5.43"?
#
# '''
# print(dados["USD"]["valor"])