# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab8C.py
import pygame, sys
from pygame.locals import *

#setup pygame window
pygame.init()
clock = pygame.time.Clock()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lab 8C Zachary Taylor')
moveSpeed = 5

#make the surface and the rect
surf = pygame.Surface((800, 600))
surf.fill((0, 0, 0))
smallRect = pygame.Rect(175, 175, 50, 50)
pygame.draw.rect(surf, (0, 0, 255), smallRect)
screen.blit(surf, (0, 0))

while True:
    playerX, playerY = smallRect.left, smallRect.top
    #keys and events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit(0) #quit if escape key is pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    
    movement = {
        pygame.K_w: (0, -moveSpeed),
        pygame.K_a: (-moveSpeed, 0),
        pygame.K_s: (0, moveSpeed),
        pygame.K_d: (moveSpeed, 0),
    }
    for key, (dirX, dirY) in movement.items():
        if keys[key]:
            new_rect = smallRect.move(dirX, dirY)
            if 0 <= new_rect.x <= width-smallRect.width and 0 <= new_rect.y <= height-smallRect.height:
                smallRect = new_rect
    if keys[pygame.K_r]:
        smallRect.x = (175) 
        smallRect.y = (175)
    
    #redraw surface
    surf.fill((0, 0, 0))
    pygame.draw.rect(surf, (0, 0, 255), smallRect)
    screen.blit(surf, (0, 0))
    pygame.display.flip()
    clock.tick(60)