'''
Escreva um programa que leia três números diferentes inseridos
pelo usuário e, utilizando estruturas condicionais, exiba na tela
qual deles é o maior e qual é o menor.

Este exercício é excelente para praticar a lógica de comparação
entre múltiplas variáveis e o uso de blocos if e else para
determinar condições de desigualdade.
'''

while True:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))

    if n1 > n2 and n1 > n3:
        print(f'O número {n1} é maior que {n2} e {n3}.')
    elif n2 > n1 and n2 > n3:
        print(f'O número {n2} é maior que {n1} e {n3}')
    else:
        print(f'O numero {n3} é maior que {n1} e {n2}')

    if n1 < n2 and n1 < n3:
        print(f'O número {n1} é menor que {n2} e {n3}')
    elif n2 < n1 and n2 < n3:
        print(f'O número {n2} é menor que {n1} e {n3}')
    else:
        print(f'O número {n3} é menor que {n1} e {n2}')

