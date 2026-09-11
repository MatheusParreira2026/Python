'''
Desafio 42 (22:36): Refaça o desafio 35 (sobre triângulos) acrescentando o tipo de triângulo:
Equilátero (todos os lados iguais), Isósceles (dois lados iguais) ou Escaleno (todos os lados diferentes).
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

print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)

r1 = float(input(f'{cores['azul']}Primeiro segmento: '))
r2 = float(input(f'{cores['azul']}Segundo segmento: '))
r3 = float(input(f'{cores['azul']}Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'{cores['verde']}Os segmentos acima podem formam um triângulo!')
    if r1 == r2 == r3:
        print(f"Os segmentos formam um triângulo equilátero.")
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print(f"Os segmentos formam um triângulo Isósceles.")
    else:
        print(f"Os segmentos forma um triângulo Escaleno.")
else:
    print(f'{cores['vermelho']}Os segmentos acima não podem formar um triângulo.{cores['limpa']}')
