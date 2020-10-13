#!/usr/bin/env python

background_image_filename = 'Naruto_background.jpg'
#**mouse_image_filename = 'Naruto_mouse.jpg'
#指定影象檔名稱

import pygame
#匯入pygame庫
from pygame.locals import *
#匯入一些常用的函式和常量
from sys import exit
#向sys模組借一個exit函式用來退出程式

pygame.init()
#初始化pygame,為使用硬體做準備

screen = pygame.display.set_mode((640, 480), 0, 32)
#建立了一個視窗
pygame.display.set_caption("Hello, Naruto!")
#設定視窗標題

background = pygame.image.load(background_image_filename).convert()
#**mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#載入並轉換影象

while True:
#遊戲主迴圈

    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件後退出程式
            exit()

    screen.blit(background, (0,0))
    #將背景圖畫上去

    x, y = pygame.mouse.get_pos()
    #獲得滑鼠位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #計算游標的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把游標畫上去

    pygame.display.update()
    #重新整理一下畫面