'''
Desafio 40 (21:33): Leia duas notas de um aluno e calcule a média. Mostre se ele está reprovado (abaixo de 5.0),
em recuperação (entre 5.0 e 6.9) ou aprovado (7.0 ou mais).
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

n1 = float(input('Digite quanto você tirou na primeira prova: '))
n2 = float(input('Digite quanto você tirou na segunda prova: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'Você tem a média de{cores['vermelho']} {media:.2f}{cores['limpa']} pontos, sendo assim está {cores['vermelho']}REPROVADO{cores['limpa']}.')
elif media < 7.0:
    print(f'Você tem a média de {cores['amarelo']}{media:.2f}{cores['limpa']} pontos, sendo assim está em {cores['amarelo']}RECUPERAÇÃO{cores['limpa']}.')
else:
    print(f'Você tem a média de {cores['verde']}{media:.2f}{cores['limpa']} pontos, sendo assim está{cores['verde']} APROVADO{cores['limpa']}.')
