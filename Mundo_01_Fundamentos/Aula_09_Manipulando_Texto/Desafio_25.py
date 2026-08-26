'''
Criar um programa que leia o nome de uma pessoa
e diga se ela tem 'Silva' no nome (em qualquer posição).
'''

nome = str(input('Digite o seu nome: '))
nome_formatado = nome.lower()
print('silva' in nome_formatado)

'''
Alternativa correta

Pontos importantes explicados no vídeo:

.strip(): Remove espaços inúteis antes e depois do nome digitado (1:30).

.lower(): Converte todo o nome para letras minúsculas, garantindo que 
a busca encontre "silva" independentemente de o usuário ter digitado 
com maiúsculas ou minúsculas (1:45).

Operador in: É uma ferramenta nativa do Python para verificar a existência
de uma substring (4:24).
'''

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
