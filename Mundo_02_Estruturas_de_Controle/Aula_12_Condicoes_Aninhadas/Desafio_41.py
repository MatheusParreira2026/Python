'''
Desafio 41 (22:00): Leia o ano de nascimento de um atleta e mostre sua categoria: Mirim (até 9 anos),
Infantil (até 14 anos), Júnior (até 19 anos), Sênior (até 20 anos) e Master (acima disso).
'''

from datetime import date

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

ano_de_nascimento = int(input('Digite o ano em que você nasceu: '))

idade = date.today().year - ano_de_nascimento

if idade <= 9:
    print(f"Sua idade de {cores['verde']}{idade} anos{cores['limpa']} corresponde a categoria {cores['verde']}Mirim{cores['limpa']}.")
elif idade <= 14:
    print(f"Sua idade de {cores['verde']}{idade} anos{cores['limpa']} corresponde a categoria {cores['verde']}Infantil{cores['limpa']}.")
elif idade <= 19:
    print(f"Sua idade de {cores['verde']}{idade} anos{cores['limpa']} corresponde a categoria {cores['verde']}Júnior{cores['limpa']}.")
elif idade <= 20:
    print(f"Sua idade de {cores['verde']}{idade} anos{cores['limpa']} corresponde a categoria {cores['verde']}Sênior{cores['limpa']}.")
else:
    print(f"Sua idade de {cores['verde']}{idade} anos{cores['limpa']} corresponde a categoria {cores['verde']}Master{cores['limpa']}.")
