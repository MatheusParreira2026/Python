'''
Desafio 37 (18:07): Escreva um programa que leia um número inteiro e peça para o usuário escolher a
base de conversão: 1 para binário, 2 para octal ou 3 para hexadecimal.
'''

# cores = {
#     # Reset
#     'limpa': '\033[m',
#
#     # Cores normais
#     'preto': '\033[30m',
#     'vermelho': '\033[31m',
#     'verde': '\033[32m',
#     'amarelo': '\033[33m',
#     'azul': '\033[34m',
#     'magenta': '\033[35m',
#     'ciano': '\033[36m',
#     'branco': '\033[37m',
#
#     # Cores claras / brilhantes
#     'cinza': '\033[90m',
#     'vermelhoclaro': '\033[91m',
#     'verdeclaro': '\033[92m',
#     'amareloclaro': '\033[93m',
#     'azulclaro': '\033[94m',
#     'magentaclaro': '\033[95m',
#     'cianoclaro': '\033[96m',
#     'brancoclaro': '\033[97m',
#
#     # Estilos
#     'negrito': '\033[1m',
#     'fraco': '\033[2m',
#     'sublinhado': '\033[4m',
#     'piscando': '\033[5m',
#     'invertido': '\033[7m',
#
#     # Combinações
#     'pretoebranco': '\033[7;97m',
# }
#
# numero = int(input('Digite um número inteiro: '))
# print(f'''\n{cores['verde'] + cores['negrito']}[1] Binário
# {cores['verde'] + cores['negrito']}[2] Octal
# {cores['verde'] + cores['negrito']}[3] Hexadecimal{cores['limpa']}''')
# opcao = int(input('\nEscolha uma das opções acima: '))
#
# if opcao == 1:
#     print(f'\nO número {cores['verde']}{numero}{cores['limpa']} em sua forma binária é igual a: {cores['verde'] + cores['negrito']}{bin(numero)}')
# elif opcao == 2:
#     print(f'\nO número {cores['verde']}{numero}{cores['limpa']} em sua forma octal é igual a: {cores['verde'] + cores['negrito']}{oct(numero)}')
# elif opcao == 3:
#     print(f'\nO número {cores['verde']}{numero}{cores['limpa']} em sua forma hexadecimal é igual a: {cores['verde'] + cores['negrito']}{hex(numero)}')


'''
Alternativa 01
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

numero = int(input('Digite um número inteiro: '))
print(f'''\n{cores['verde'] + cores['negrito']}[1] Binário
{cores['verde'] + cores['negrito']}[2] Octal
{cores['verde'] + cores['negrito']}[3] Hexadecimal{cores['limpa']}''')
opcao = int(input('\nEscolha uma das opções acima: '))

if opcao == 1:
    resultado = bin(numero)
    base = 'binária'
elif opcao == 2:
    resultado = oct(numero)
    base = 'octal'
elif opcao == 3:
    resultado = hex(numero)
    base = 'hexadecimal'
elif opcao != 1 and 2 and 3:
    print('Digite uma opção válida.')

print(f'\nO número {cores['verde']}{numero}{cores['limpa']} em sua forma {cores['verde']}{base}{cores['limpa']} é igual a: {cores['verde']}{resultado}{cores['limpa']}')
