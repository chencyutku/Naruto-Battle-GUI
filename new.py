background_image_filename = 'Naruto_background.jpg'
mouse_image_filename = 'cursor_PNG101.png'
#選擇背景以及鼠標圖

#匯入需要的函示庫
import pygame
from pygame.locals import *
from sys import exit
#from math import pi

#初始化pygame
pygame.init()

#建立遊戲視窗
screen = pygame.display.set_mode((640, 480), 0, 32)
#設定遊戲視窗上標題
pygame.display.set_caption("Naruto game home page")

#載入並轉換影象(可使載入更快)
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

#顏色可以先定義好之後使用比較方便
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)

#render方法返回Surface物件
fontObj = pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj = fontObj.render('S T A R T',True,GREEN,BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center=(320,320)

while True:
    #遊戲主迴圈

    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件後退出程式
            exit()

    screen.blit(background, (0,0))

    #顯示"開始遊戲"文字
    screen.blit(textSurfaceObj,textRectObj)

    x, y = pygame.mouse.get_pos()
    #獲得滑鼠位置
    x-= mouse_cursor.get_width() / 10
    y-= mouse_cursor.get_height() / 10
    #計算游標的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把游標畫上去

    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            mouse_down=event.button
            mouse_down_70,mouse_down_250=event.pos

    #重新整理一下畫面
    pygame.display.update()
