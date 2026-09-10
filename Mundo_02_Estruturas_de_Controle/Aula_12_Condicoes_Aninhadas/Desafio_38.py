'''
Desafio 38 (19:39): Leia dois números inteiros e compare-os, mostrando se o primeiro é maior,
o segundo é maior ou se não existe valor maior (são iguais).
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

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print(f"O número{cores['verde']} {n1} {cores['limpa']}é maior que {cores['verde']}{n2}{cores['limpa']}.")
elif n2 > n1:
    print(f"O número{cores['verde']} {n2} {cores['limpa']}é maior que {cores['verde']}{n1}{cores['limpa']}.")
else:
    print(f"Os números {cores['verde']}{n1}{cores['limpa']} e {cores['verde']}{n2}{cores['limpa']} são iguais.")
