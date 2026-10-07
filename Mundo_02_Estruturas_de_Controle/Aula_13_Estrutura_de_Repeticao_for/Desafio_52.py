'''
DESAFIO 052

Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.
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

numero = int(input("Digite um número inteiro: "))

total_divisores = 0

if numero > 1:
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            total_divisores += 1
    if total_divisores == 2:
        print("É primo.")
    else:
        print("Não é primo.")
else:
    print("Digite um número maior que 1.")
