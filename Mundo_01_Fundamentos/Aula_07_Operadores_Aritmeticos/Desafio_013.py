'''
Faça um algoritmo que leia o salário de um
funcionário e mosntre seu novo salário, com
15% de aumento.
'''

salario = float(input('Digite o seu salário atual: '))
aumento = (salario * 0.15) + salario
print(f'O seu novo salário com um aumento de 15% é: R${aumento:.2f}')
