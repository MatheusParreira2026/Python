'''
Desenvolva de um programa para calcular o preço da passagem
de uma viagem de ônibus, com base na distância percorrida em quilômetros:

Viagens curtas (até 200 km): O preço cobrado é de R$ 0,50 por quilômetro rodado.

Viagens longas (acima de 200 km): O preço reduz para R$ 0,45 por quilômetro rodado.

O objetivo é utilizar a estrutura condicional if e else para aplicar a taxa correta
conforme a distância fornecida pelo usuário.
'''

# distancia = float(input('Diga a distância percorrida na sua viagem: '))
# if distancia <= 200:
#     preco = distancia * 0.50
#     print(f'Você fez uma viagem curta e percorreu {distancia:.2f}km. Valor a ser pago: R$ {preco:.2f}')
# else:
#     preco = distancia * 0.45
#     print(f'Você fez uma viagem longa e percorreu {distancia:.2f}km. Valor a ser pago: R$ {preco:.2f}')

'''
Exemplo 01 feito pelo professor
Solução com estrutura condicional (if/else)
Esta é a forma mais comum, utilizando um bloco if para verificar 
a distância e calcular o preço conforme o enunciado (02:16 - 03:40):
'''
# distancia = float(input('Qual é a distância da sua viagem? '))
# print(f'Você está prestes a começar uma viagem de {distancia}Km.')
#
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
#
# print(f'E o preço da sua passagem será de R${preco:.2f}')

'''
Exemplo 02 feito pelo professor
Solução simplificada (operador ternário)
O professor também mostra como fazer o mesmo cálculo de forma mais 
compacta, utilizando uma estrutura de if inline (05:04 - 05:21):
'''
distancia = float(input('Qual é a distância da sua viagem? '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O preço da sua passagem será de R${preco:.2f}')
