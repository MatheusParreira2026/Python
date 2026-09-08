'''
Desafio 36 (17:03): Crie um programa para aprovar um empréstimo bancário. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal e negue o empréstimo se ela
exceder 30% do salário.
'''

cores = {
    # Reset
    'limpa': '\033[m',

    # Cores normais
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    # Cores claras / brilhantes
    'cinza': '\033[90m',
    'vermelhoclaro': '\033[91m',
    'verdeclaro': '\033[92m',
    'amareloclaro': '\033[93m',
    'azulclaro': '\033[94m',
    'magentaclaro': '\033[95m',
    'cianoclaro': '\033[96m',
    'brancoclaro': '\033[97m',

    # Estilos
    'negrito': '\033[1m',
    'fraco': '\033[2m',
    'sublinhado': '\033[4m',
    'piscando': '\033[5m',
    'invertido': '\033[7m',

    # Combinações
    'pretoebranco': '\033[7;97m',
}

valor_casa = float(input('Qual o valor da sua casa? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos  = int(input('Em quantos anos você pretende pagar? '))

prestacao_mensal = valor_casa / (anos * 12)
trinta_por_cento_do_salario = salario * 30 / 100

print(f'\nA sua prestação mensal corresponde a R$ {prestacao_mensal:.2f}')
print(f'\n30% do seu salário corresponde a R$ {trinta_por_cento_do_salario:.2f}')

if prestacao_mensal > trinta_por_cento_do_salario:
    print(f"{cores['vermelho'] + cores['negrito']}\nEmpréstimo NEGADO")
else:
    print(f"{cores['verde'] + cores['negrito']}\nEmpréstimo APROVADO")
