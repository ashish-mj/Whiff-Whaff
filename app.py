#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:15:24 2020

@author: ashish
"""

import pygame,sys,random



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

ball_speed_x = 6 * random.choice((1,-1))
ball_speed_y = 6 * random.choice((1,-1))
player_speed, cpu_speed = 0,6

def ball_movement():
    
    global ball_speed_x,ball_speed_y
    
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y
    
    if ball.top <=0 or ball.bottom>= screen_height:
        ball_speed_y *= -1
    if ball.left <=0 or ball.right>= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1
 
def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height    
    
def cpu_movement():
    if cpu.top < ball.y:
        cpu.top += cpu_speed
    if cpu.bottom > ball.y:
        cpu.bottom -= cpu_speed
    if cpu.top <= 0:
        cpu.top=0
    if cpu.bottom >=screen_height:
        cpu.bottom =screen_height
        
def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
    
    ball_movement()
    player_movement()
    cpu_movement()
    
    screen.fill(background)
    pygame.draw.rect(screen,border,player)
    pygame.draw.rect(screen,border,cpu)
    pygame.draw.ellipse(screen,border,ball)
    pygame.draw.aaline(screen,border,(screen_width/2,0),(screen_width/2,screen_height))
    pygame.display.flip()
    clock.tick(60)
    
            