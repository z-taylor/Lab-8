# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab8A.py
import pygame, sys
from pygame.locals import *

#setup pygame window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Lab 8A Zachary Taylor')

#make the surface and the rects
surf = pygame.Surface((800, 600))
surf.fill((0, 0, 0))

smallRect = pygame.Rect(0, 0, 50, 50)
pygame.draw.rect(surf, (0, 0, 255), smallRect)
longRect = pygame.Rect(175, 0, 50, 400)
pygame.draw.rect(surf, (255, 0, 0), longRect)

screen.blit(surf, (0, 0))

flip = False
while True:
    #keys and events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit(0) #quit if escape key is pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    #Moving square
    if smallRect.left <= 0:
        flip = False
    elif smallRect.right >= 400:
        flip = True
    if flip:
        smallRect = smallRect.move(-5, 0)
    else:
        smallRect = smallRect.move(5, 0)

    #redraw surface
    surf.fill((0, 0, 0))
    pygame.draw.rect(surf, (0, 0, 255), smallRect)
    pygame.draw.rect(surf, ( (0, 255, 0) if longRect.colliderect(smallRect) else (255, 0, 0) ), longRect)
    screen.blit(surf, (0, 0))
    pygame.display.flip()
    clock.tick(60)