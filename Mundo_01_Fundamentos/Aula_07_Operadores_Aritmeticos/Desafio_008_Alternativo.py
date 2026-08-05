'''
Escreva um programa que leia um valor em metros
e o exiba convertido para quilômetros, hectômetros,
decâmetros, decímetros, centímetros e milímetros.

'''

metros = float(input('Digite um valor em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(f'{metros} metros convertido para quilômetros é igual a: {km:.0f} km')
print(f'{metros} metros convertido para hectômetros é igual a: {hm:.0f} hm')
print(f'{metros} metros convertido para decâmetros é igual a: {dam:.0f} dam')
print(f'{metros} metros convertido para decímetros é igual a: {dm:.0f} dm')
print(f'{metros} metros convertido para centímetros é igual a: {cm:.0f} cm')
print(f'{metros} metros convertido para milímetros é igual a: {mm:.0f} mm')
