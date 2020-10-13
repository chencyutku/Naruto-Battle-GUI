#利用鍵盤方向鍵使背景圖片移動
background_image_filename = 'Naruto_background.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
#background = pygame.image.load(background_image_filename).convert()
background = pygame.image.load(background_image_filename).convert()
x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           exit()
        if event.type == KEYDOWN:
            #鍵盤有按下？
            if event.key == K_LEFT:
                #按下的是左方向鍵的話，把x座標減一
                move_x = -1
            elif event.key == K_RIGHT:
                #右方向鍵則加一~
                move_x = 1
            elif event.key == K_UP:
                #類似了
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            #如果使用者放開了鍵盤，圖就不要動了
            move_x = 0
            move_y = 0

        #計算出新的座標
        x+= move_x
        y+= move_y

        screen.fill((0,0,0))
        screen.blit(background, (x,y))
        #在新的位置上畫圖
        pygame.display.update()