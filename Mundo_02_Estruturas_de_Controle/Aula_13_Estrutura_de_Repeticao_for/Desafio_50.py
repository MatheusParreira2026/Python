'''
DESAFIO 050

Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
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
soma = 0
for n in range(0, 6):
    entrada = int(input("Digite um número inteiro: "))
    if entrada % 2 == 0:
        soma += entrada
print(f"A soma dos seis números pares inteiros é igual a: {soma}")


'''
Alternativa incorreta (modificar futuramente)
'''
# soma = 0
# entrada = int(input("Digite um número inteiro: "))
# if entrada % 2 == 0:
#     for n2 in range(0, 5):
#         entrada_02 = int(input("Digite outro número inteiro: "))
#         if entrada % 2 == 0:
#             soma += entrada
# print(f"A soma dos números pares inteiros é igual a: {soma}")
