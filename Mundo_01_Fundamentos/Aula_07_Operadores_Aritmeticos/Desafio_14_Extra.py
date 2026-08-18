'''
Escreva um programa que converta uma temperatura digitada em ºC
e converta para ºF.
'''

celsius = float(input('Dgite a temperatura em graus Celsius: '))
celsius_para_fahrenheit = celsius * 9 / 5 + 32
print(f'{celsius:.2f}ºC equivale a {celsius_para_fahrenheit:.2f}ºF')


