'''
Escreva um programa que leia a velocidade de um carro.
As regras são:

Limite de velocidade: 80 km/h.

Condição: Se o carro ultrapassar esse limite, ele
deve exibir uma mensagem informando que o motorista foi multado.

Cálculo da multa: O programa deve calcular o valor da multa, que custa
R$ 7,00 por cada km/h que exceder o limite.

Se o carro estiver a 80 km/h ou menos, o programa não deve mostrar
nenhuma mensagem de multa.
'''

velocidade = float(input('Informe a velocidade atual do carro: '))

if velocidade > 80:
    excesso_de_velocidade = (velocidade - 80) * 7
    print(f'Você foi multado! O valor da sua multa é de: R$ {excesso_de_velocidade:.2f}.')
else:
    print(f'Sua velocidade é de {velocidade:.2f}km/h. Essa velocidade está dentro do limite.')

'''
Alternativa feita pelo professor
'''
# velocidade = float(input('Qual é a velocidade atual do carro? '))
# if velocidade > 80:
#     print('Multado! Você excedeu o limite permitido de 80km/h')
#     multa = (velocidade - 80) * 7
#     print(f'Você deve pagar uma multa de R${multa:.2f}')
#
#     print('Tenha um bom dia! Dirija com segurança')
#