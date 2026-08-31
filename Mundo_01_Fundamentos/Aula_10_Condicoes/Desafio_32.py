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

# from datetime import date
# ano = int(input('Digite um ano qualquer ou 0 para o ano atual: '))
# if ano == 0:
#     ano = date.today().year
# if ano % 400 == 0:
#     print(f'O ano {ano} é um ano bissexto.')
# elif ano % 100 == 0:
#     print(f'O ano {ano} não é um ano bissexto.')
# elif ano % 4 == 0:
#     print(f'O ano {ano} é um ano bissexto.')
# else:
#     print(f'O ano {ano} não é um ano bissexto.')

'''
Exemplo feito pelo professor

O código utiliza a biblioteca datetime para obter o ano atual 
caso o usuário digite 0, e aplica a lógica matemática necessária
para identificar anos bissextos (divisível por 4, mas não por 
100, a menos que também seja divisível por 400).
'''
from datetime import date
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} NÃO é bissexto")
