'''
Criar um programa que leia o nome completo de
uma pessoa e mostre separadamente o primeiro e
o último nome.
'''

# nome_completo = str(input('Digite o seu nome completo: '))
# primeiro_nome = nome_completo.split()[0]
# ultimo_nome = nome_completo.split()[-1]
# print(f'O seu primeiro nome é {primeiro_nome}')
# print(f'O seu úlimo nome é {ultimo_nome}')

'''
Alternativa correta

Explicação dos comandos:

strip() (02:17): Remove espaços indesejados antes e depois do nome digitado.

split() (02:30): Divide a string em uma lista de palavras baseada nos espaços.

nome[0] (03:13): Acessa o primeiro elemento da lista (o primeiro nome).

len(nome)-1 (04:47): Calcula o tamanho total da lista e subtrai 1 para
encontrar o índice do último elemento, garantindo que o programa funcione
 independentemente do tamanho do nome (05:22).
'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')