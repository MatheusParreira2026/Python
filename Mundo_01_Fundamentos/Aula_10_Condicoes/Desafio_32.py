'''
Crie um programa que leia um ano qualquer fornecido pelo usuário
e determine se ele é um ano bissexto ou não.

Para resolver este exercício, você deve:
Pesquisar e entender as regras matemáticas que definem um ano
bissexto no calendário gregoriano.

Implementar essas regras utilizando a estrutura condicional (if e else)
em Python para exibir a resposta correta.
'''

# ano =int(input('Digite um ano qualquer: '))
#
# if ano % 400 == 0:
#     print(f'O ano {ano} é um ano bissexto.')
# elif ano % 100 == 0:
#     print(f'O ano {ano} não é um ano bissexto.')
# elif ano % 4 == 0:
#     print(f'O ano {ano} é um ano bissexto.')

from datetime import date
ano = int(input('Digite um ano qualquer ou 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto.')
elif ano % 100 == 0:
    print(f'O ano {ano} não é um ano bissexto.')
elif ano % 4 == 0:
    print(f'O ano {ano} é um ano bissexto.')
else:
    print(f'O ano {ano} não é um ano bissexto.')
