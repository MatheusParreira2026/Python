'''
criar um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento salarial com base em faixas de renda:
Salários superiores a R$ 1.250,00: Aplicar um aumento de 10%.

Salários inferiores ou iguais a R$ 1.250,00: Aplicar um aumento de 15%.

O objetivo é utilizar a estrutura condicional (if e else) para determinar
a porcentagem correta e calcular o novo valor do salário do funcionário.
'''

salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    aumento_de_dez_por_cento = (salario * 10 / 100) + salario
    print(f'''O seu salário de {salario:.2f} é acima de R$ 1.250,00. Sendo assim você tem direito 
a um aumento de 10%, o seu salário agora é de R$ {aumento_de_dez_por_cento:.2f}''')
elif salario <= 1250:
    aumento_de_quinze_por_cento = (salario * 15 / 100) + salario
    print(f'''O seu salário de R$ {salario:.2f} é abaixo ou igual a R$ 1.250,00. Sendo assim você tem direito 
a um aumento de 15%, o seu salário agora é de R$ {aumento_de_quinze_por_cento:.2f}.''')
