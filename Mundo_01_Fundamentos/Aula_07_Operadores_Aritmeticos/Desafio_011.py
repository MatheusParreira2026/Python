'''
Faça um programa que leia a largura e a altura de uma
parede em metros, calcule a sua área e a quantidade de
de tinta necessária para pintá-la, sabendo que cada litro
de tinta, pinta uam área de 2 metros quadrados.
'''

largura = float(input("Informe em metros a largura da parede: "))
altura = float(input("Informe em metros a altura da parede: "))

area = largura * altura
litros = (largura * altura) / 2

print(f'Sua parede tem a dimensão de {largura:.2f}x{litros:.2f} e sua área é de {area:.2f}m²')
print(f'Será necessário {litros:.2f} litros de tinta para pintar a parede.')
