'''
Escreva um programa que leia um valor
em metros e o exiba convertido em
centímetros e milímetros.
'''

metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mm = metros * 1000
print(f'O valor {metros:.2f} metros em centímetros é igual a: {cm:.0f} cm')
print(f'O valor {metros:.2f} metros em milímetros é igual a: {mm:.0f} mm')
