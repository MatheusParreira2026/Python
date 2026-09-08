'''
Aula 12 | Condições Aninhas
Link: https://www.youtube.com/watch?v=j9bYDjaAYzw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=3

Nesta aula do Curso de Python, o professor Gustavo Guanabara apresenta o conceito de condições aninhadas,
um passo fundamental no segundo mundo do curso (0:09-0:14).

Pontos principais do vídeo:

O que são estruturas aninhadas: O professor utiliza a analogia de caminhos em uma estrada para explicar que,
ao lidar com problemas mais complexos, não temos apenas opções binárias (verdadeiro ou falso). Podemos
colocar uma estrutura condicional dentro de outra para criar múltiplas possibilidades (02:22-04:45).

Sintaxe em Python: A estrutura utiliza os comandos if, elif (uma simplificação de else if) e else. O professor
enfatiza a importância da indentação e dos dois pontos (:) no final de cada linha de comando para que o
código funcione corretamente (08:47-09:15).

Regras de uso: É possível utilizar quantos elif forem necessários, enquanto o else é opcional e pode ser utilizado
apenas uma vez ao final da estrutura (09:55-10:25).

Prática: O professor demonstra um exemplo prático no PyCharm, criando um programa que analisa diferentes nomes
e retorna mensagens baseadas em condições aninhadas (10:50-15:20).

Desafios: A aula termina com a proposta de 10 desafios para fixação do conteúdo (do exercício 36 ao 45), incluindo
problemas de empréstimo bancário, conversão de bases numéricas, cálculo de IMC e um jogo de Jokenpô (16:00-26:20).
'''

'''
Exemplo 01 | Estrutura Condicional Aninhada

O professor Gustavo Guanabara apresenta o exemplo prático mais completo de uma estrutura condicional
aninhada entre (13:06-15:20) do vídeo. O código utiliza uma série de condições (if, elif e else)
para analisar o conteúdo de uma variável chamada nome:
'''

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))