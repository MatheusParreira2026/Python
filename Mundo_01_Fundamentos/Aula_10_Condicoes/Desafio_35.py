'''
Desenvolva um programa que leia o comprimento
de três retas e verifique se elas podem ou não
formar um triângulo.

Para resolver este problema, você precisará pesquisar
o princípio matemático (a desigualdade triangular)
que define as condições necessárias para que três
segmentos de reta formem um triângulo.
O professor enfatiza que entender essa lógica é o passo principal
antes de implementar o código, que será testado usando
as estruturas condicionais if e else aprendidas nesta aula.
'''

reta_A = float(input('Digite o comprimento da 1ª reta: '))
reta_B = float(input('Digite o comprimento da 2ª reta: '))
reta_C = float(input('Digite o comprimento da 3ª reta: '))

if (reta_A < (reta_B + reta_C)) and (reta_B < (reta_A + reta_C)) and (reta_C < (reta_A + reta_B)):
    print('Triângulo pode ser formado.')
else:
    print('Triângulo não pode ser formado.')