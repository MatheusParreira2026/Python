'''
Link: https://www.youtube.com/watch?v=0hBIhkcA8O8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=48

Aula 11 | Cores no Terminal

Nesta aula do Curso em Vídeo, o professor Gustavo Guanabara encerra
o primeiro mundo (fundamentos) ensinando como adicionar cores ao
terminal utilizando Python. O conteúdo principal foca no uso de
códigos de escape ANSI para personalizar a saída de texto no terminal.
'''

'''
Exemplo 01
Letra em vermelho
'''
# print('\033[31mOlá, Mundo!')

'''
Exemplo 02
Letra vermelha, fundo amarelo
'''
# print('\033[31;43mOlá, Mundo!')

'''
Exemplo 03
Letra vermelha em negrito, com fundo amarelo
'''
# print('\033[1;31;43mOlá, Mundo!')

'''
Exemplo 04
Letra vermelha em negrito, com fundo amarelo sem listra amarela até o final no terminal
'''
# print('\033[1;31;43mOlá, Mundo!\033[m')

'''
Exemplo 05
Letra branca em negrito, com fundo lilás sem listra 
amarela até o final no terminal e com sublinhado
'''
# print('\033[1;97;45mOlá, Mundo!\033[m')

'''
Exemplo 06
Cor invertida (preto e branco)
'''
# print('\033[7;97mOlá, Mundo!\033[m')

'''
Exemplo 07
Cor invertida (amarelo e azul)
'''
# print('\033[7;33;44mOlá, Mundo!\033[m')

'''
Exemplo 08
Cores em partes específicas do código
'''
# a = 3
# b = 5
# print('Os valores são \033[32m{} \033[m e \033[31m{} \033[m !!!'.format(a, b))

'''
Exemplo 09
Cores no format
'''
# nome = 'Guanabara'
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

'''
Exemplo 10
Dicionário de cores
'''
nome = 'Guanabara'
cores = {
'limpa': '\033[m',
'azul': '\033[34m',
'amarelo': '\033[33m',
'pretoebranco': '\033[7;97m'
}
print('Olá, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))