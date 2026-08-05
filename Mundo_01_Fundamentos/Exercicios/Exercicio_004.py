'''
Faça um programa que leia algo pelo
teclado e mostre na tela seu tipo
primitivo e todas as informações sobre ele.
'''

entrada = input("Digite algo: ")

print(f'\nO tipo primitivo de {entrada} é ', type(entrada))

print(f'\n{entrada} possui letras e todas elas estão em maiúsculas?')
print('Resposta:', entrada.isupper())

print(f'\n{entrada} possui letras e todas elas estão em minúsculas?')
print('Resposta:', entrada.islower())

print(f'\n{entrada} contém somente letras?')
print('Resposta:', entrada.isalpha())

print(f'\n{entrada} contém somente dígitos?')
print('Resposta:', entrada.isdigit())

print(f'\n{entrada} contém somente caracteres decimais?')
print('Resposta:', entrada.isdecimal())

print(f'\n{entrada} contém somente caracteres numéricos?')
print('Resposta:', entrada.isnumeric())

print(f'\n{entrada} contém somente letras e/ou números?')
print('Resposta:', entrada.isalnum())

print(f'\n{entrada} contém somente espaços?')
print('Resposta:', entrada.isspace())

print(f'\n{entrada} está no formato de título?')
print('Resposta:', entrada.istitle())

print(f'\n{entrada} contém somente caracteres ASCII?')
print('Resposta:', entrada.isascii())

print(f'\n{entrada} pode ser usado como identificador Python?')
print('Resposta:', entrada.isidentifier())

print(f'\n{entrada} tem todos os caracteres imprimíveis?')
print('Resposta:', entrada.isprintable())

'''
Alternativo
'''

# entrada = input("Digite algo: ")
#
# print('\nO tipo primitivo de {} é {}'.format(entrada, type(entrada)))
#
# print('\n{} possui letras e todas elas estão em maiúsculas?'.format(entrada))
# print('Resposta:', entrada.isupper())
#
# print('\n{} possui letras e todas elas estão em minúsculas?'.format(entrada))
# print('Resposta:', entrada.islower())
#
# print('\n{} contém somente letras?'.format(entrada))
# print('Resposta:', entrada.isalpha())
#
# print('\n{} contém somente dígitos?'.format(entrada))
# print('Resposta:', entrada.isdigit())
#
# print('\n{} contém somente caracteres decimais?'.format(entrada))
# print('Resposta:', entrada.isdecimal())
#
# print('\n{} contém somente caracteres numéricos?'.format(entrada))
# print('Resposta:', entrada.isnumeric())
#
# print('\n{} contém somente letras e/ou números?'.format(entrada))
# print('Resposta:', entrada.isalnum())
#
# print('\n{} contém somente espaços?'.format(entrada))
# print('Resposta:', entrada.isspace())
#
# print('\n{} está no formato de título?'.format(entrada))
# print('Resposta:', entrada.istitle())
#
# print('\n{} contém somente caracteres ASCII?'.format(entrada))
# print('Resposta:', entrada.isascii())
#
# print('\n{} pode ser usado como identificador Python?'.format(entrada))
# print('Resposta:', entrada.isidentifier())
#
# print('\n{} tem todos os caracteres imprimíveis?'.format(entrada))
# print('Resposta:', entrada.isprintable())

