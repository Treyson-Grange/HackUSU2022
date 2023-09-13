import pygame
import random

def generateEnemy(screen, numAttacks, textList, spritePath):


    #["Talk to your Ducky", "Eval is Evil!", "Scrum Meeting!", "Cheating is bad!!!"]
    font = pygame.font.Font('Assets/Fonts/Pixeltype.ttf', 30)
    enemy_surf = pygame.transform.scale2x(pygame.image.load(str(spritePath))).convert_alpha()
    enemy_rect = enemy_surf.get_rect(center = (700,275))
    if numAttacks == 0:
        enemy_speech = font.render(str(textList[0]),False,(225,225,225))
    elif numAttacks == 1:
        enemy_speech = font.render(str(textList[1]), False, (225, 225, 225))
    elif numAttacks == 2:
        enemy_speech = font.render(str(textList[2]), False, (225, 225, 225))
    else:
        enemy_speech = font.render(str(textList[3]), False, (225, 225, 225))


    enemy_speech_rect = enemy_speech.get_rect(center = (700,200))
    screen.blit(enemy_surf,enemy_rect)

    screen.blit(enemy_speech,enemy_speech_rect)