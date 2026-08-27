'''
Desenvolva de um programa para calcular o preço da passagem
de uma viagem de ônibus, com base na distância percorrida em quilômetros:

Viagens curtas (até 200 km): O preço cobrado é de R$ 0,50 por quilômetro rodado.

Viagens longas (acima de 200 km): O preço reduz para R$ 0,45 por quilômetro rodado.

O objetivo é utilizar a estrutura condicional if e else para aplicar a taxa correta
de acordo com a distância fornecida pelo usuário.
'''

distancia = float(input('Diga a distância percorrida na sua viagem: '))
if distancia <= 200:
    preco_viagem_curta = distancia * 0.50
    print(f'Você fez uma viagem curta e percorreu {distancia:.2f}km. Valor a ser pago: R$ {preco_viagem_curta:.2f}')
else:
    preco_viagem_longa = distancia * 0.45
    print(f'Você fez uma viagem longa e percorreu {distancia:.2f}km. Valor a ser pago: R$ {preco_viagem_longa:.2f}')
