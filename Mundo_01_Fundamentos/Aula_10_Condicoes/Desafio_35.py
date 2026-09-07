'''
Desenvolva um programa que leia o comprimento
de três retas e verifique se elas podem ou não
formar um triângulo.

Para resolver este problema, você precisará pesquisar
o princípio matemático (a desigualdade triangular)
que define as condições necessárias para que três
segmentos de reta formem um triângulo.
O professor enfatiza que entender essa lógica é o passo principal
antes de implementar o código, que será testado usando
as estruturas condicionais if e else aprendidas nesta aula.
'''

# reta_A = float(input('Digite o comprimento da 1ª reta: '))
# reta_B = float(input('Digite o comprimento da 2ª reta: '))
# reta_C = float(input('Digite o comprimento da 3ª reta: '))
#
# if (reta_A < (reta_B + reta_C)) and (reta_B < (reta_A + reta_C)) and (reta_C < (reta_A + reta_B)):
#     print('Triângulo pode ser formado.')
# else:
#     print('Triângulo não pode ser formado.')

'''
Exercício feito pelo professor
Link: https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=47
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

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'{cores['verde']}Os segmentos acima podem formar um triângulo!')
else:
    print(f'{cores['vermelho']}Os segmentos acima não podem formar um triângulo.')
