'''
Crie um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo e calcule e mostre o comprimento da hipotenusa.

DICA: é possível resolver esse desafio de forma simples utilizando recursos de módulos matemáticos,
aplicando o princípio de que o quadrado da hipotenusa é igual à soma dos quadrados dos catetos.
'''
import math

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
print(f'A hipotenusa é igual {hipotenusa:.2f}')
