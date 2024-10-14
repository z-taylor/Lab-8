# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab8B.py
import pygame, sys
from pygame.locals import *

#setup pygame window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Lab 8B Zachary Taylor')

#make the surface and the rects
surf = pygame.Surface((800, 600))
surf.fill((0, 0, 0))

smallRect1 = pygame.Rect(0, 0, 50, 50)
pygame.draw.rect(surf, (0, 0, 255), smallRect1)
smallRect2 = pygame.Rect(0, 175, 50, 50)
pygame.draw.rect(surf, (0, 0, 255), smallRect2)
smallRect3 = pygame.Rect(0, 350, 50, 50)
pygame.draw.rect(surf, (0, 0, 255), smallRect3)
rectList = [smallRect1, smallRect2, smallRect3]
longRect = pygame.Rect(175, 0, 50, 400)
pygame.draw.rect(surf, (255, 0, 0), longRect)

screen.blit(surf, (0, 0))

flip1 = False
flip2 = False
flip3 = False
while True:
    #keys and events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit(0) #quit if escape key is pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    #Moving square 1
    if smallRect1.left <= 0:
        flip1 = False
    elif smallRect1.right >= 400:
        flip1 = True
    if flip1:
        smallRect1 = smallRect1.move(-10, 0)
    else:
        smallRect1 = smallRect1.move(10, 0)

    #Moving square 2
    if smallRect2.left <= 0:
        flip2 = False
    elif smallRect2.right >= 400:
        flip2 = True
    if flip2:
        smallRect2 = smallRect2.move(-5, 0)
    else:
        smallRect2 = smallRect2.move(5, 0)

    #Moving square 3
    if smallRect3.left <= 0:
        flip3 = False
    elif smallRect3.right >= 400:
        flip3 = True
    if flip3:
        smallRect3 = smallRect3.move(-20, 0)
    else:
        smallRect3 = smallRect3.move(20, 0)

    rectList = [smallRect1, smallRect2, smallRect3]

    #redraw surface
    surf.fill((0, 0, 0))
    pygame.draw.rect(surf, (0, 0, 255), smallRect1)
    pygame.draw.rect(surf, (0, 0, 255), smallRect2)
    pygame.draw.rect(surf, (0, 0, 255), smallRect3)
    pygame.draw.rect(surf, ( (0, 255, 0) if longRect.collidelistall(rectList) != [] else (255, 0, 0) ), longRect)
    screen.blit(surf, (0, 0))
    pygame.display.flip()
    clock.tick(60)