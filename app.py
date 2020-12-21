#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:15:24 2020

@author: ashish
"""

import pygame,sys

pygame.init()
clock = pygame.time.Clock()


screen_width = 1260
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping Pong')

ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
cpu = pygame.Rect(10,screen_height/2-70,10,140)

background = pygame.Color('grey12')
border = (200,200,200)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.fill(background)
    pygame.draw.rect(screen,border,player)
    pygame.draw.rect(screen,border,cpu)
    pygame.draw.ellipse(screen,border,ball)
    pygame.draw.aaline(screen,border,(screen_width/2,0),(screen_width/2,screen_height))
    pygame.display.flip()
    clock.tick(60)
    
            