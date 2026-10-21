'''
DESAFIO 056

Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas.
Ao final, o programa deve exibir três informações:

A média de idade do grupo;
O nome do homem mais velho;
Quantas mulheres têm menos de 21 anos.
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
acumulador_de_idades = 0
for pessoa in range(1, 5):
    nome = str(input(f"{pessoa}ª pessoa, digite o seu nome: "))
    idade = int(input(f"{pessoa}ª pessoa, digite sua idade: "))
    sexo = str(input(f"""{pessoa}ª pessoa, Informe o seu sexo,
digite 'M' pra masculino e 'F' para feminino: """)).replace(" ", "").lower()
    acumulador_de_idades += idade
media = acumulador_de_idades / 4
print(f"A media das idades é de {media} anos.")