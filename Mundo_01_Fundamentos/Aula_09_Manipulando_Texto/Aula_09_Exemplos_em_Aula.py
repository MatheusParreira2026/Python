'''
Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), transformações
com replace(), upper(), lower(), capitalize(), title(), strip(),
junção com join().
'''
'''
Exemplo Base
'''
# frase = 'Curso em Vídeo Python'
# print(frase)

'''
Fatiamento | Exemplo 01
'''
# frase = 'Curso em Vídeo Python'
# print(frase[3])

'''
Fatiamento | Exemplo 02
'''
# frase = 'Curso em Vídeo Python'
# print(frase[3:13])

'''
Fatiamento | Exemplo 03
'''
# frase = 'Curso em Vídeo Python'
# print(frase[:13])

'''
Fatiammento | Exemplo 04
'''
# frase = 'Curso em Vídeo Python'
# print(frase[13:])

'''
Fatimento | Exemplo 05
'''
# frase = 'Curso em Vídeo Python'
# print(frase[1:15])

'''
Fatiamento | Exemplo 06
'''
# frase = 'Curso em Vídeo Python'
# print(frase[1:15:2])

'''
Fatiamento | Exemplo 07
'''
# frase = 'Curso em Vídeo Python'
# print(frase[1::2])

'''
Fatiamento | Exemplo 08
'''
# frase = 'Curso em Vídeo Python'
# print(frase[::2])

'''
Exemplo de "print" em texto com mútiplas
linhas.
'''
# print('''Alan Turing foi um matemático, lógico e cientista da computação britânico.
# Ele é considerado um dos pioneiros da ciência da computação e da inteligência artificial.
# Durante a Segunda Guerra Mundial, ajudou a decifrar códigos secretos da Alemanha nazista.
# Turing também criou importantes conceitos teóricos sobre máquinas e computação.
# Seu trabalho teve grande influência no desenvolvimento dos computadores modernos.
# ''')

'''
Análise | Exemplo 01
'''
# frase = 'Curso em Vídeo Python'
# print(frase.count('o'))

'''
Análise | Exemplo 02
'''
# frase = 'Curso em Vídeo Python'
# print(frase.count('O'))

'''
Análise e Transformações | Exemplo 01
'''
# frase = 'Curso em Vídeo Python'
# print(frase.upper().count('O'))

'''
Análise | Exemplo 03
'''
# frase = 'Curso em Vídeo Python'
# print(len(frase))

'''
Análise | Exemplo 04
'''
# frase = '   Curso em Vídeo Python   '
# print(len(frase))

'''
Análise e Transformações | Exemplo 02
'''
# frase = '   Curso em Vídeo Python   '
# print(len(frase.strip()))

'''
Transformações | Exemplo 01
'''
# frase = 'Curso em Vídeo Python'
# print(frase.replace('Python', 'Android'))

'''
Exemplo de imutabilidade da String
'''
# frase = 'Curso em Vídeo Python'
# frase[0] = '3'

'''
Exemplo que demonstra que o método replace()
não altera a String original.
O resultado da substituição é uma nova String,
que precisa ser armazenada ou utilizada para que
a substituição tenha efeito.
'''
# frase = 'Curso em Vídeo Python'
# frase.replace('Python', 'Android')
# print(frase)

'''
Exemplo que demonstra que o método replace()
retorna uma nova String com a substituição.
Ao atribuir esse resultado novamente à variável
frase, passamos a trabalhar com a nova String.
'''
# frase = 'Curso em Vídeo Python'
# frase = frase.replace('Python', 'Android')
# print(frase)

'''
Exemplo em que o operador "in" verifica se uma 
determinada sequência de caracteres está presente
dentro de outra string.
Como existe, o resultado é "True"
'''
# frase = 'Curso em Vídeo Python'
# print('Curso' in frase)

'''
Análise | Exemplo 05
'''
# frase = 'Curso em Vídeo Python'
# print(frase.find('Curso'))

'''
Análise | Exemplo 06
'''
# frase = 'Curso em Vídeo Python'
# print(frase.find('Vídeo'))

'''
Análise | Exemplo 07
'''
# frase = 'Curso em Vídeo Python'
# print(frase.find('vídeo'))

'''
Análise e Transformações | Exemplo 03
'''
# frase = 'Curso em Vídeo Python'
# print(frase.lower().find('vídeo'))

'''
Fatiamento | Exemplo 09
'''
# frase = 'Curso em Vídeo Python'
# print(frase.split())

'''
Fatiamento | Exemplo 10
'''
# frase = 'Curso em Vídeo Python'
# divido = frase.split()
# print(divido)

'''
Fatiamento | Exemplo 10
'''
# frase = 'Curso em Vídeo Python'
# divido = frase.split()
# print(divido[0])

'''
Fatiamento | Exemplo 10
'''
# frase = 'Curso em Vídeo Python'
# divido = frase.split()
# print(divido[2][3])