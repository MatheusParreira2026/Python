'''
Link da Aula-> https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=39

Pontos principais discutidos:

Estrutura Sequencial vs. Condicional: Até o momento, os programas seguiam
um caminho único (de cima para baixo). O professor utiliza a analogia de
um carro em uma estrada com bifurcações para explicar que, na programação,
podemos criar desvios baseados em decisões (1:37 - 5:35).

Comandos If e Else: O comando if (se) define um bloco de código que só é executado
se uma condição for verdadeira (13:52).

O comando else (senão) define o caminho alternativo caso
a condição do if seja falsa (14:19).

Indentação: O Python utiliza a indentação (o recuo do código
usando a tecla TAB) para identificar quais blocos de comandos
pertencem a cada estrutura (13:30 - 13:45).

Sintaxe Básica: A importância fundamental de utilizar os
dois pontos (:) ao final das linhas de if e else (13:58 - 14:27).

Condição Simplificada: Apresentação de uma forma mais compacta de
escrever condições em uma única linha, semelhante ao operador
ternário de outras linguagens (18:00 - 19:14).
'''

'''
Exemplo 01 | if

O primeiro exemplo prático desta aula (20:46 - 22:45) foca
na criação de uma estrutura condicional simples para interagir
 com o nome do usuário.
'''
# nome = str(input('Qual é o seu nome? ')).strip()
# if nome == 'Matheus':
#     print('Seu nome é muito lindo!')
# print(f'Olá {nome}!')

'''
Exemplo 02 | if e else
'''
# nome = str(input('Qual é o seu nome? ')).strip()
# if nome == 'Matheus':
#     print('Seu nome é muito lindo!')
# else:
#     print('Seu nome é tão normal...')
# print(f'Olá {nome}!')

'''
Exemplo 03 | Cálculo de média com if e else
'''

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda  nota: '))
# media = (n1 + n2) / 2
# print(f'Sua media é {media}')
# if media >= 6.0:
#     print('Parabéns você foi aprovado!')
# else:
#     print('Você está reprovado.')

'''
Exemplo 04 | Condição simplificada
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda  nota: '))
media = (n1 + n2) / 2
print(f'Sua media é {media}')
print('Parabéns' if media >= 6 else 'ESTUDE MAIS!')
