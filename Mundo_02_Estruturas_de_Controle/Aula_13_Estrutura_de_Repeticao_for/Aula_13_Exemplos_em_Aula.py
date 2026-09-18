"""
Aula 13 | Laços de Repetição (Parte 1)

Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for", que é
uma estrutura versátil e simples de entender.

Link: https://www.youtube.com/watch?v=cL4YDtFnCt4&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=14
"""

'''
Exemplo 01

Pode-se simplificar o seu código utilizando a estrutura
de repetição for em vez de escrever a mesma linha várias vezes.
'''
# print("oi")
# print("oi")
# print("oi")
# print("oi")
# print("oi")
# print("oi")

'''
Exemplo 02

Neste exemplo, o comando print("Oi") está indentado (recuado), o
que significa que ele faz parte do laço for. O Python executará
esse comando repetidamente para cada valor no intervalo definido
por range(0, 6), ou seja, 6 vezes
'''
# for c in range(0, 6):
#     print("Oi")
# print("FIM")

'''
Exemplo 03

Ao indentar (recuar) o comando print("FIM") para dentro do laço for,
ele passa a fazer parte da estrutura de repetição. Em vez de ser 
executado apenas uma vez ao final, o Python irá repetir o comando 
print("FIM") a cada iteração do laço, junto com o print("Oi").
'''
# for c in range(0, 6):
#     print("Oi")
#     print("FIM")

'''
Exemplo 04
Demonstra o uso da estrutura de repetição for em Python para realizar
uma contagem e imprimir valores sequenciais.
'''
# for c in range(0, 6):
#     print(c)
# print("FIM")

'''
Exemplo 05

Ao utilizar range(1, 6), você define um contador c que percorre
os números começando em 1 e parando antes de chegar ao 6 (ou seja, 1, 2, 3, 4 e 5).
'''
# for c in range(1, 6):
#     print(c)
# print("FIM")

'''
Exemplo 06

O range no Python ignora o último valor definido,
 o que é um ponto comum de confusão para iniciantes
'''
# for c in range(1, 7):
#     print(c)
# print("FIM")

'''
Exemplo 07

Este código demonstra como realizar uma contagem 
regressiva utilizando o laço for.
'''
# for c in range(6, 0, -1):
#     print(c)
# print("FIM")

'''
Exemplo 08

range(0, 7, 2) gera números de 0 até antes de 7,
 pulando de 2 em 2: 0, 2, 4, 6.
O for imprime cada número, e depois que o laço termina,
print("FIM") é executado.
'''
# for c in range(0, 7, 2):
#     print(c)
# print("FIM")

'''
Exemplo 09

O código solicita que o usuário digite um número inteiro no terminal.
Depois, ele exibe na tela uma sequência de 0 até o número anterior ao 
digitado.
Por fim, o programa imprime a palavra 'FIM' para indicar o término da execução.
'''
# n = int(input('Digite um número: '))
# for c in range(0, n):
#     print(c)
# print('FIM')

'''
Exemplo 10

O usuário digita n, e o for imprime os números de 0 até n,
incluindo o próprio n por causa do + 1.
Depois que o for termina, print('FIM') é executado.
'''
# n = int(input('Digite um número: '))
# for c in range(0, n + 1):
#     print(c)
# print('FIM')

'''
Exemplo 11

O usuário define início (i), fim (f) e passo (p), e o
for percorre esses valores usando range(i, f+1, p), incluindo o f.
A cada repetição, c recebe o próximo valor e é impresso; ao terminar, imprime FIM.
'''
# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')

'''
Exemplo 12

O for repete 3 vezes (0, 1, 2), e em cada repetição pede ao usuário um valor inteiro,
armazenando-o em n.
Depois das 3 entradas, o for termina e o programa imprime fim.
'''
# for c in range(0, 3):
#     n = int(input('Digite um valor: '))
# print('fim')

'''
Exemplo 13

O código começa s = 0 e, durante 4 repetições, lê um valor em n e soma esse valor
ao acumulador s usando s += n.
No final, .format(s) coloca o valor da soma dentro da mensagem, mostrando a 
soma de todos os 4 valores digitados.
'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))

