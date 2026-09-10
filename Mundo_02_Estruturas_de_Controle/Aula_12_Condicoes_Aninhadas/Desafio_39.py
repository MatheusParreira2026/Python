'''
Desafio 39 (20:11): Leia o ano de nascimento de um jovem e informe se ele ainda vai se alistar ao serviço militar,
se é a hora exata ou se já passou do prazo. O programa deve mostrar quanto tempo falta ou quanto tempo passou
do prazo.
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

if idade == 18:
    print(f'Você tem {cores['verde']}{idade}{cores['verde']} anos{cores['limpa']} de idade, portanto deve se alistar.')
elif idade > 18:
    prazo = idade - 18
    print(f'Você tem {cores['verde']}{idade} anos{cores['limpa']} de idade, sendo assim se passaram {prazo} anos para efetuar o alistamento.')
else:
    prazo = 18 - idade
    print(f'Você tem {cores['verde']}{idade} ano(s){cores['limpa']} de idade, você deve esperar {prazo} anos para se alistar.')
