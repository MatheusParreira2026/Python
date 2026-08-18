'''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa
R$60 por dia e R$0,15 por Km rodado.
'''

km = float(input('Quantos quilômetros o seu carro percorreu? '))
dias = int(input('Quantos dias o senhor(a) usou o carro? '))

preco_por_dia = dias * 60
preco_por_km = km * 0.15
preco_total = preco_por_dia + preco_por_km

print(f'O valor total a ser pago é de R$ {preco_total:.2f}')
