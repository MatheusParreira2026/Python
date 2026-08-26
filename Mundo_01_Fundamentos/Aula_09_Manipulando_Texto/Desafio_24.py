'''
Criar um programa que leia o nome de uma cidade e
verifique se ela começa ou não com o nome 'Santo'.
'''

# cidade = str(input('Digite o nome de uma cidade: '))
# print(f"Verificador: {cidade.startswith('Santo')}")

'''
Alternativa correta

Explicação das funções utilizadas:

.strip() (3:45): Remove todos os espaços vazios indesejados antes
e depois do nome da cidade digitada pelo usuário.

cid[:5] (2:15): Fatiamento que seleciona apenas os 5 primeiros 
caracteres da string (letras 0 a 4)

.upper() (4:15): Converte o texto para letras maiúsculas,
garantindo que a comparação funcione independentemente de como
o usuário tenha digitado a palavra.
'''
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
