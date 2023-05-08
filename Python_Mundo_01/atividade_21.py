#Exercício Python 21: 
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
mp3 = "c:\som.mp3"

pygame.mixer.music.load(mp3)
pygame.mixer.music.play()
pygame.event.wait()
