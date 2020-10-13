import pygame
from pygame.locals import *
from sys import exit
#模組初始化
pygame.init()
#建立一個視窗，視窗大小為640*480
screen=pygame.display.set_mode([640,480])
#定義視窗的標題為'Draw'
pygame.display.set_caption('game window')
#用白色填充視窗
screen.fill((40,40,40))


#pygame.draw.circle(screen,[255,255,255],[60,85],50,0)
#pygame.draw.circle(screen,[255,255,255],[580,85],50,0)

pygame.draw.rect(screen,[255,255,255],[50,165,200,200],0)
pygame.draw.rect(screen,[255,255,255],[380,165,200,200],0)

pygame.draw.rect(screen,[255,255,255],[30,395,240,60],0)
pygame.draw.rect(screen,[255,255,255],[365,395,240,60],0)

# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 30)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('Player1 Point:', True, (255, 255, 255))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
screen.blit(text_surface, (10, 10))

# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 30)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('Player2 Point:', True, (255, 255, 255))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
screen.blit(text_surface, (450, 10))

small_sa=pygame.image.load('D://temp//demo//sa_small_circle.png')
small_sa.convert()
screen.blit(small_sa, (-25, -15))

small_sa=pygame.image.load('D://temp//demo//na_small_circle.png')
small_sa.convert()
screen.blit(small_sa, (455, 30))


pygame.display.update()

while True:
    #遊戲主迴圈

    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件後退出程式
            exit()

    #pygame.display.update()