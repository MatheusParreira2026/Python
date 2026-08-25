'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

DICA: A solução envolve obrigatoriamente o uso de módulos. O desafio aqui não
é apenas processar dados, mas interagir com arquivos de mídia externos. A
dica fundamental é pesquisar por bibliotecas ou módulos que permitam o controle
de reprodução de áudio, pois o Python base não possui essa funcionalidade integrada
por padrão. Você precisará encontrar o módulo correto, importá-lo e configurar o caminho
do arquivo de áudio para que o programa consiga executá-lo.
'''
# from playsound3 import playsound
#
# playsound("04. Moth Into Flame.mp3")

'''
Alternativa 01
'''
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("04. Moth Into Flame.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)